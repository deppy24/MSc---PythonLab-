import re
import json
import datetime
import os
from tkinter import *
from dateutil.relativedelta import relativedelta  # Για προσθήκη ενός μήνα

#Η ενοικιαση θεσησ χρεωνεται κατα την εισοδο , η ωραιαια κατα την εξοδο. Μετα απο ενα μηνα η θεση ελευθερωνεται αυτοματα.

# Ορισμός κανονικής έκφρασης για έλεγχο αριθμού κυκλοφορίας.
# Αποδεκτό μοτίβο: ακριβώς 3 γράμματα (Α-Ω ή A-Z) ακολουθούμενα από παύλα και 4 ψηφία.
license_plate_pattern = re.compile(r'^[A-ZΑ-Ω]{3}-\d{4}$')

# =================== Κλάση για το αυτοκίνητο ======================
class Auto:
    def __init__(self, license_plate, driver_name=None):
        self.license_plate = license_plate
        self.driver_name = driver_name

# =================== Κλάση για τη θέση στάθμευσης ======================
class ParkingSpot:
    def __init__(self, number, reserved=False):
        self.number = number           # Αριθμός θέσης
        self.reserved = reserved       # Αν είναι δεσμευμένη (μακροχρόνια) ή όχι
        self.occupied = False          # Κατοχυρωμένη ή ελεύθερη
        self.auto = None               # Το αυτοκίνητο που σταθμεύει (αν υπάρχει)
        self.entry_time = None         # Ώρα/ημερομηνία εισόδου ή έναρξης ενοικίασης
        self.rental_end = None         # Ημερομηνία λήξης ενοικίασης (μόνο για μακροχρόνιες)
        self.long_term = False         # Flag που υποδεικνύει μακροχρόνια στάθμευση

# =================== Κύρια κλάση διαχείρισης πάρκινγκ ======================
class ParkingManagement:
    def __init__(self):
        self.spots = []          # Λίστα θέσεων στάθμευσης
        self.transactions = []   # Λίστα κινήσεων (εισερχόμενα, εξερχόμενα, ενοικιάσεις)
        self.revenue_hourly = 0.0      # Συνολικές εισπράξεις για ωριαία στάθμευση
        self.revenue_longterm = 0.0    # Συνολικές εισπράξεις για μακροχρόνιες/ενοικιάσεις
        self.init_spots()
        self.load_data()

    def init_spots(self):
        """
        Δημιουργεί 20 θέσεις στάθμευσης. Οι 5 πρώτες είναι δεσμευμένες για μακροχρόνια στάθμευση.
        """
        for i in range(1, 21):
            if i <= 5:
                spot = ParkingSpot(i, reserved=True)
            else:
                spot = ParkingSpot(i, reserved=False)
            self.spots.append(spot)

    def load_data(self):
        """
        Φορτώνει τα δεδομένα κατοχής θέσεων, εισπράξεων και κινήσεων από αρχείο (αν υπάρχει).
        """
        if os.path.exists('parking_data.json'):
            try:
                with open('parking_data.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for spot_data in data.get("spots", []):
                        num = spot_data["number"]
                        spot = self.spots[num-1]
                        spot.occupied = spot_data["occupied"]
                        spot.reserved = spot_data["reserved"]
                        spot.long_term = spot_data["long_term"]
                        entry_time = spot_data.get("entry_time")
                        spot.entry_time = datetime.datetime.fromisoformat(entry_time) if entry_time else None
                        rental_end = spot_data.get("rental_end")
                        spot.rental_end = datetime.datetime.fromisoformat(rental_end) if rental_end else None
                        if spot.occupied and spot_data.get("license_plate"):
                            spot.auto = Auto(spot_data["license_plate"], spot_data.get("driver_name"))
                    self.revenue_hourly = data.get("revenue_hourly", 0)
                    self.revenue_longterm = data.get("revenue_longterm", 0)
                    self.transactions = data.get("transactions", [])
            except Exception as e:
                print("Σφάλμα φόρτωσης δεδομένων:", e)

    def save_data(self):
        """
        Αποθηκεύει τα δεδομένα των θέσεων, εισπράξεων και κινήσεων σε αρχείο JSON.
        """
        data = {
            "spots": [],
            "revenue_hourly": self.revenue_hourly,
            "revenue_longterm": self.revenue_longterm,
            "transactions": self.transactions
        }
        for spot in self.spots:
            spot_data = {
                "number": spot.number,
                "reserved": spot.reserved,
                "occupied": spot.occupied,
                "long_term": spot.long_term,
                "license_plate": spot.auto.license_plate if spot.auto else None,
                "driver_name": spot.auto.driver_name if (spot.auto and spot.auto.driver_name) else None,
                "entry_time": spot.entry_time.isoformat() if spot.entry_time else None,
                "rental_end": spot.rental_end.isoformat() if spot.rental_end else None
            }
            data["spots"].append(spot_data)
        with open('parking_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def update_expired_rentals(self):
        """
        Ελέγχει και απελευθερώνει τις δεσμευμένες θέσεις για τις οποίες έχει λήξει η περίοδος ενοικίασης.
        """
        now = datetime.datetime.now()
        updated = False
        for spot in self.spots:
            if spot.reserved and spot.occupied and spot.rental_end is not None:
                if now >= spot.rental_end:
                    print(f"[Ενημέρωση] Η μακροχρόνια ενοικίαση για τη θέση {spot.number} (Αυτοκίνητο {spot.auto.license_plate}) έληξε. Η θέση απελευθερώθηκε.")
                    spot.occupied = False
                    spot.auto = None
                    spot.entry_time = None
                    spot.rental_end = None
                    spot.long_term = False
                    updated = True
        if updated:
            self.save_data()

    def validate_license_plate(self, plate):
        """
        Ελέγχει αν ο αριθμός κυκλοφορίας είναι σε σωστό μοτίβο.
        """
        return bool(license_plate_pattern.match(plate))

    def is_plate_in_use(self, plate):
        """
        Ελέγχει αν η πινακίδα χρησιμοποιείται ήδη σε κάποια κατειλημμένη θέση.
        """
        for spot in self.spots:
            if spot.occupied and spot.auto and spot.auto.license_plate == plate:
                return True
        return False

    def find_free_spot(self, long_term=False):
        """
        Επιστρέφει μία ελεύθερη θέση ανάλογα με τον τύπο στάθμευσης.
        Αν long_term==True αναζητεί μία από τις δεσμευμένες θέσεις.
        """
        if long_term:
            for spot in self.spots:
                if spot.reserved and not spot.occupied:
                    return spot
            return None
        else:
            for spot in self.spots:
                if (not spot.reserved) and (not spot.occupied):
                    return spot
            return None

    def count_long_term(self):
        """
        Μετράει πόσες δεσμευμένες (μακροχρόνιες/ενοικιασμένες) θέσεις είναι κατειλημμένες.
        """
        return sum(1 for spot in self.spots if spot.reserved and spot.occupied)

    def earliest_long_term_end(self):
        """
        Επιστρέφει την ημερομηνία λήξης της μακροχρόνιας ενοικίασης που λήγει πρώτη.
        """
        ends = [spot.rental_end for spot in self.spots if spot.reserved and spot.occupied and spot.rental_end]
        return min(ends) if ends else None

    # =================== Μέθοδοι για τις επιλογές μενού ======================

    def εισερχόμενο(self):
        """
        Διαδικασία εισόδου αυτοκινήτου στο πάρκινγκ.
        Για ωριαία στάθμευση (τύπος 2) λειτουργεί όπως πριν.
        Για μακροχρόνια (τύπος 1), ζητούνται επιπλέον στοιχεία (όνομα οδηγού, επιλογή θέσης και ημερομηνία έναρξης ενοικίασης)
        και η συμπεριφορά είναι ανάλογη της επιλογής ενοικίασης θέσης.
        """
        self.update_expired_rentals()
        print("\n=== Εισερχόμενο Αυτοκίνητο ===")
        plate = input("Εισάγετε αριθμό κυκλοφορίας (π.χ. ΚΛΜ-4245): ").upper().strip()
        if not self.validate_license_plate(plate):
            print("[Σφάλμα] Ο αριθμός κυκλοφορίας δεν έχει το σωστό format (π.χ. ΚΛΜ-4245).")
            return
        if self.is_plate_in_use(plate):
            print(f"[Σφάλμα] Το αυτοκίνητο με την πινακίδα {plate} είναι ήδη παρκαρισμένο.")
            return

        typ = input("Επιλέξτε τύπο στάθμευσης: [1] Μακροχρόνια (Ενοικίαση θέσης, 50€ για 1 μήνα) ή [2] Ωριαία (2€/ώρα): ").strip()
        if typ not in ['1', '2']:
            print("[Σφάλμα] Η επιλογή που εισάγατε δεν είναι έγκυρη. Επιλέξτε 1 ή 2.")
            return
        now = datetime.datetime.now()
        if typ == '1':
            # Μακροχρόνια στάθμευση μέσω εισερχόμενων: ζητούνται επιπλέον στοιχεία για την ενοικίαση.
            print("[Ενημέρωση] Επιλέξατε μακροχρόνια ενοικίαση. Παρακαλώ δώστε τα επιπλέον στοιχεία.")
            driver = input("Εισάγετε όνομα οδηγού: ").strip()
            try:
                chosen_spot = int(input("Εισάγετε αριθμό θέσης που επιθυμείτε (1-20): ").strip())
            except:
                print("[Σφάλμα] Ο αριθμός θέσης πρέπει να είναι ακέραιος μεταξύ 1 και 20.")
                return
            if not (1 <= chosen_spot <= 20):
                print("[Σφάλμα] Ο αριθμός θέσης πρέπει να είναι μεταξύ 1 και 20.")
                return
            spot = self.spots[chosen_spot-1]
            if spot.occupied or not spot.reserved:
                alt_spot = self.find_free_spot(long_term=True)
                if not alt_spot:
                    print("[Αποτυχία] Δεν υπάρχουν διαθέσιμες δεσμευμένες θέσεις για ενοικίαση.")
                    return
                print(f"[Ενημέρωση] Η θέση {chosen_spot} δεν είναι διαθέσιμη. Ανατίθεται αυτόματα η θέση {alt_spot.number}.")
                spot = alt_spot

            if self.count_long_term() >= 5:
                next_free = self.earliest_long_term_end()
                if next_free:
                    print(f"[Απορριπτέο] Έχετε φτάσει στο όριο των 5 μακροχρόνιων ενοικιάσεων. Η πιο σύντομη λήξη είναι στις {next_free.strftime('%d/%m/%Y %H:%M:%S')}.")
                else:
                    print("[Απορριπτέο] Δεν υπάρχουν διαθέσιμες δεσμευμένες θέσεις.")
                return

            today = datetime.datetime.now().date()
            start_date_str = input(f"Εισάγετε ημερομηνία έναρξης ενοικίασης (ηη/μμ/εεεε, από {today.strftime('%d/%m/%Y')} και μετά): ").strip()
            try:
                start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
                if start_date < today:
                    print("[Σφάλμα] Η ημερομηνία έναρξης δεν μπορεί να είναι πριν από σήμερα.")
                    return
            except Exception as e:
                print(f"[Σφάλμα] Μη έγκυρη μορφή ημερομηνίας. Χρησιμοποιήστε το format ηη/μμ/εεεε. Λεπτομέρειες: {e}")
                return
            start_datetime = datetime.datetime.combine(start_date, datetime.time.min)
            end_datetime = start_datetime + relativedelta(months=1)

            spot.auto = Auto(plate, driver)
            spot.occupied = True
            spot.long_term = True
            spot.entry_time = start_datetime
            spot.rental_end = end_datetime
            self.revenue_longterm += 50
            self.transactions.append({
                "type": "εισερχόμενο-ενοικίαση",
                "plate": plate,
                "driver": driver,
                "spot": spot.number,
                "start": start_date.strftime("%d/%m/%Y"),
                "end": end_datetime.strftime("%d/%m/%Y"),
                "amount": 50,
                "message": "Εισερχόμενο μακροχρόνια ενοικίαση: άμεση χρέωση 50€."
            })
            print(f"[Επιτυχία] Η θέση {spot.number} ενοικιάστηκε για το αυτοκίνητο {plate}.\n  Η έναρξη είναι στις {start_date.strftime('%d/%m/%Y')} και η λήξη στις {end_datetime.strftime('%d/%m/%Y')}.")
        else:
            # Ωριαία στάθμευση
            spot = self.find_free_spot(long_term=False)
            if not spot:
                print("[Αποτυχία] Δεν υπάρχουν διαθέσιμες θέσεις ωριαίας στάθμευσης.")
                return
            auto = Auto(plate)
            spot.auto = auto
            spot.occupied = True
            spot.long_term = False
            spot.entry_time = now
            self.transactions.append({
                "type": "εισερχόμενο-ωριαίο",
                "plate": plate,
                "spot": spot.number,
                "time": now.isoformat(),
                "amount": 0,
                "message": "Ωριαία στάθμευση: εισαγωγή χωρίς άμεση χρέωση."
            })
            print(f"[Επιτυχία] Το αυτοκίνητο {plate} σταθμεύτηκε στη θέση {spot.number} για ωριαία στάθμευση.")
        self.save_data()

    def εξερχόμενο(self):
        """
        Διαδικασία εξόδου αυτοκινήτου από το πάρκινγκ.
        Για ωριαία στάθμευση υπολογίζεται η χρέωση (2€/ώρα) με στρογγυλοποίηση προς τα πάνω.
        Για μακροχρόνιες, δεν γίνεται επιπλέον χρέωση.
        """
        self.update_expired_rentals()
        print("\n=== Εξερχόμενο Αυτοκίνητο ===")
        plate = input("Εισάγετε αριθμό κυκλοφορίας: ").upper().strip()
        if not self.validate_license_plate(plate):
            print("[Σφάλμα] Ο αριθμός κυκλοφορίας δεν είναι έγκυρος.")
            return
        found = None
        for spot in self.spots:
            if spot.occupied and spot.auto and spot.auto.license_plate == plate:
                found = spot
                break
        if not found:
            print(f"[Σφάλμα] Δεν βρέθηκε το αυτοκίνητο με την πινακίδα {plate} στο πάρκινγκ.")
            return
        now = datetime.datetime.now()
        if found.long_term:
            print(f"[Ενημέρωση] Το αυτοκίνητο {plate} αφορά μακροχρόνια στάθμευση. Δεν πραγματοποιείται επιπλέον χρέωση.")
            self.transactions.append({
                "type": "εξερχόμενο-μακροχρόνια",
                "plate": plate,
                "spot": found.number,
                "time": now.isoformat(),
                "amount": 0,
                "message": "Έξοδος μακροχρόνιας στάθμευσης."
            })
        else:
            diff = now - found.entry_time
            hours = diff.total_seconds() / 3600
            hours = int(hours) + (1 if (hours - int(hours)) > 0 else 0)
            fee = hours * 2
            self.revenue_hourly += fee
            self.transactions.append({
                "type": "εξερχόμενο-ωριαίο",
                "plate": plate,
                "spot": found.number,
                "time": now.isoformat(),
                "hours": hours,
                "amount": fee,
                "message": f"Ωριαία στάθμευση: {hours} ώρα(ες) x 2€ = {fee}€."
            })
            print(f"[Επιτυχία] Χρεώθηκαν {fee}€ για {hours} ώρα(ες) ωριαίας στάθμευσης.")
        # Απελευθέρωση της θέσης
        found.occupied = False
        found.auto = None
        found.entry_time = None
        found.rental_end = None
        found.long_term = False
        self.save_data()

    def ενοικίαση(self):
        """
        Διαδικασία ενοικίασης θέσης (αν εκτελεστεί ξεχωριστά).
        Ζητούνται όλα τα απαραίτητα στοιχεία όπως στην εισερχόμενη μακροχρόνια ενοικίαση.
        """
        self.update_expired_rentals()
        print("\n=== Ενοικίαση Θέσης ===")
        plate = input("Εισάγετε αριθμό κυκλοφορίας (π.χ. ΚΛΜ-4245): ").upper().strip()
        if not self.validate_license_plate(plate):
            print("[Σφάλμα] Ο αριθμός κυκλοφορίας δεν πληροί το απαιτούμενο format (π.χ. ΚΛΜ-4245).")
            return
        if self.is_plate_in_use(plate):
            print(f"[Σφάλμα] Το αυτοκίνητο με την πινακίδα {plate} είναι ήδη παρκαρισμένο στο σύστημα.")
            return
        driver = input("Εισάγετε όνομα οδηγού: ").strip()
        try:
            chosen_spot = int(input("Εισάγετε αριθμό θέσης που επιθυμείτε (1-20): ").strip())
        except:
            print("[Σφάλμα] Ο αριθμός θέσης πρέπει να είναι ακέραιος μεταξύ 1 και 20.")
            return
        if not (1 <= chosen_spot <= 20):
            print("[Σφάλμα] Ο αριθμός θέσης πρέπει να είναι μεταξύ 1 και 20.")
            return
        spot = self.spots[chosen_spot-1]
        if spot.occupied or not spot.reserved:
            alt_spot = self.find_free_spot(long_term=True)
            if not alt_spot:
                print("[Αποτυχία] Δεν υπάρχουν διαθέσιμες δεσμευμένες θέσεις για ενοικίαση.")
                return
            print(f"[Ενημέρωση] Η θέση {chosen_spot} δεν είναι διαθέσιμη. Ανατίθεται αυτόματα η θέση {alt_spot.number}.")
            spot = alt_spot

        if self.count_long_term() >= 5:
            next_free = self.earliest_long_term_end()
            if next_free:
                print(f"[Απορριπτέο] Έχετε φτάσει στο όριο των 5 μακροχρόνιων ενοικιάσεων. Η πιο σύντομη λήξη είναι στις {next_free.strftime('%d/%m/%Y %H:%M:%S')}.")
            else:
                print("[Απορριπτέο] Δεν υπάρχουν διαθέσιμες δεσμευμένες θέσεις.")
            return

        today = datetime.datetime.now().date()
        start_date_str = input(f"Εισάγετε ημερομηνία έναρξης ενοικίασης (ηη/μμ/εεεε, από {today.strftime('%d/%m/%Y')} και μετά): ").strip()
        try:
            start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
            if start_date < today:
                print("[Σφάλμα] Η ημερομηνία έναρξης δεν μπορεί να είναι πριν από σήμερα.")
                return
        except Exception as e:
            print(f"[Σφάλμα] Μη έγκυρη μορφή ημερομηνίας. Χρησιμοποιήστε το format ηη/μμ/εεεε. Λεπτομέρειες: {e}")
            return
        start_datetime = datetime.datetime.combine(start_date, datetime.time.min)
        end_datetime = start_datetime + relativedelta(months=1)

        spot.auto = Auto(plate, driver)
        spot.occupied = True
        spot.long_term = True
        spot.entry_time = start_datetime
        spot.rental_end = end_datetime
        self.revenue_longterm += 50
        self.transactions.append({
            "type": "ενοικίαση",
            "plate": plate,
            "driver": driver,
            "spot": spot.number,
            "start": start_date.strftime("%d/%m/%Y"),
            "end": end_datetime.strftime("%d/%m/%Y"),
            "amount": 50,
            "message": "Ενοικίαση θέσης: άμεση χρέωση 50€."
        })
        print(f"[Επιτυχία] Η θέση {spot.number} ενοικιάστηκε για το αυτοκίνητο {plate}.\n  Η έναρξη είναι στις {start_date.strftime('%d/%m/%Y')} και η λήξη στις {end_datetime.strftime('%d/%m/%Y')}.")
        self.save_data()

    def ταμείο_ημέρας(self):
        """
        Εμφανίζει αναλυτικά τις κινήσεις εισπράξεων και το σύνολο με φιλική μορφή.
        """
        print("\n=== Ταμείο Ημέρας ===")
        total = self.revenue_hourly + self.revenue_longterm
        print("-------------------------------------------------------------")
        print("{:<25}{:<10}{:<15}".format("Τύπος Συναλλαγής", "Ποσό (€)", "Λεπτομέρειες"))
        print("-------------------------------------------------------------")
        for trans in self.transactions:
            t_type = trans.get("type", "")
            amount = trans.get("amount", 0)
            msg = trans.get("message", "")
            print("{:<25}{:<10}{:<15}".format(t_type, str(amount), msg))
        print("-------------------------------------------------------------")
        print(f"Σύνολο Εισπράξεων: {total}€")
        print("-------------------------------------------------------------")

    def προβολή_θέσεων(self):
        """
        Γραφική απεικόνιση των θέσεων στάθμευσης.
        Οι δεσμευμένες θέσεις εμφανίζονται με διαφορετικό χρώμα.
        """
        self.update_expired_rentals()
        print("\n=== Προβολή Θέσεων Στάθμευσης (Γραφικά) ===")
        root = Tk()
        root.title("Θέσεις Στάθμευσης - Parking Volos")
        for idx, spot in enumerate(self.spots):
            row = idx // 5
            col = idx % 5
            if spot.occupied:
                text = f"Θέση {spot.number}\n{spot.auto.license_plate}"
            else:
                text = f"Θέση {spot.number}\n(κενή)"
            if spot.reserved:
                bg = "orange" if spot.occupied else "lightblue"
            else:
                bg = "red" if spot.occupied else "lightgreen"
            lbl = Label(root, text=text, bg=bg, width=12, height=6, relief="ridge", borderwidth=2)
            lbl.grid(row=row, column=col, padx=5, pady=5)
        root.mainloop()

    def λίστα_παρκαρισμένων(self):
        """
        Εμφανίζει τη λίστα με τα παρκαρισμένα αυτοκίνητα και τη θέση τους.
        """
        self.update_expired_rentals()
        print("\n=== Λίστα Παρκαρισμένων Αυτοκινήτων ===")
        found = False
        for spot in self.spots:
            if spot.occupied and spot.auto:
                print(f"Θέση {spot.number}: {spot.auto.license_plate} (Οδηγός: {spot.auto.driver_name if spot.auto.driver_name else 'N/A'})")
                found = True
        if not found:
            print("Δεν υπάρχουν παρκαρισμένα αυτοκίνητα.")
        print("=== Τέλος Λίστας ===")

    def λίστα_ελεύθερων(self):
        """
        Εμφανίζει τους αριθμούς των ελεύθερων θέσεων.
        """
        self.update_expired_rentals()
        print("\n=== Λίστα Ελεύθερων Θέσεων ===")
        free_spots = [spot.number for spot in self.spots if not spot.occupied]
        if free_spots:
            print("Ελεύθερες θέσεις:", free_spots)
        else:
            print("Δεν υπάρχουν ελεύθερες θέσεις.")

    def καλύτερος_πελάτης(self):
        """
        Εμφανίζει τον/τους καλύτερο(υς) πελάτη(ες) βάσει του αριθμού καταχωρήσεων.
        Αν όλοι έχουν ίσο αριθμό καταχωρήσεων εμφανίζεται σχετικό σχόλιο.
        """
        self.update_expired_rentals()
        print("\n=== Καλύτερος Πελάτης ===")
        counts = {}
        for trans in self.transactions:
            plate = trans.get("plate")
            if plate:
                counts[plate] = counts.get(plate, 0) + 1
        if not counts:
            print("Δεν υπάρχουν δεδομένα για τους πελάτες.")
            return
        max_count = max(counts.values())
        best_plates = [plate for plate, cnt in counts.items() if cnt == max_count]
        if len(best_plates) == len(counts):
            print("[Σχόλιο] Όλοι οι πελάτες έχουν τον ίδιο αριθμό καταχωρήσεων.")
        elif len(best_plates) == 1:
            print(f"Καλύτερος πελάτης: {best_plates[0]} με {max_count} καταχωρήσεις.")
        else:
            print(f"Καλύτεροι πελάτες: {', '.join(best_plates)} με {max_count} καταχωρήσεις.")

    def συνολικές_εισπράξεις(self):
        """
        Εμφανίζει τις συνολικές εισπράξεις για μακροχρόνιες/ενοικιάσεις και ωριαίες στάθμευσεις.
        """
        self.update_expired_rentals()
        print("\n=== Συνολικές Εισπράξεις ===")
        print(f"Εισπράξεις για μακροχρόνιες/ενοικιάσεις: {self.revenue_longterm}€")
        print(f"Εισπράξεις για ωριαίες: {self.revenue_hourly}€")

# =================== Κύρια Συνάρτηση (Main) ======================
def main():
    parking = ParkingManagement()
    while True:
        print("\n--- Μενού Εφαρμογής Parking Volos ---")
        print("1. Εισερχόμενο αυτοκίνητο")
        print("2. Εξερχόμενο αυτοκίνητο")
        print("3. Ενοικίαση θέσης")
        print("4. Ταμείο ημέρας")
        print("5. Προβολή Θέσεων Στάθμευσης")
        print("6. Λίστα παρκαρισμένων αυτοκινήτων")
        print("7. Λίστα ελεύθερων θέσεων")
        print("8. Καλύτερος πελάτης")
        print("9. Συνολικές εισπράξεις")
        print("0. Έξοδος")
        choice = input("Επιλέξτε επιλογή: ").strip()
        if choice == '1':
            parking.εισερχόμενο()
        elif choice == '2':
            parking.εξερχόμενο()
        elif choice == '3':
            parking.ενοικίαση()
        elif choice == '4':
            parking.ταμείο_ημέρας()
        elif choice == '5':
            parking.προβολή_θέσεων()
        elif choice == '6':
            parking.λίστα_παρκαρισμένων()
        elif choice == '7':
            parking.λίστα_ελεύθερων()
        elif choice == '8':
            parking.καλύτερος_πελάτης()
        elif choice == '9':
            parking.συνολικές_εισπράξεις()
        elif choice == '0':
            print("Έξοδος από το πρόγραμμα. Ευχαριστούμε που χρησιμοποιήσατε την εφαρμογή Parking Volos!")
            break
        else:
            print("[Σφάλμα] Μη έγκυρη επιλογή. Παρακαλώ δοκιμάστε ξανά.")

if __name__ == "__main__":
    main()
