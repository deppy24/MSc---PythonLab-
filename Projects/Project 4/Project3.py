import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import csv
from datetime import datetime, timedelta

class FurnitureStoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Κατάστημα Επίπλων")
        
        self.orders = []

        # Κεντρικό Μενού
        main_menu = tk.Menu(self.root)
        self.root.config(menu=main_menu)

        order_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label="Παραγγελίες", menu=order_menu)
        order_menu.add_command(label="Νέα Παραγγελία", command=self.new_order)
        order_menu.add_command(label="Ακύρωση Παραγγελίας", command=self.cancel_order)
        order_menu.add_command(label="Προβολή Παραγγελιών", command=self.view_orders)
        order_menu.add_command(label="Καλύτερος Πελάτης", command=self.best_customer)

    def new_order(self):
        order_window = tk.Toplevel(self.root)
        order_window.title("Νέα Παραγγελία")

        # Αυτόματη Ημερομηνία Παραγγελίας
        order_date = datetime.now().strftime("%Y-%m-%d")
        order_number = len(self.orders) + 1  # Μοναδικός Αριθμός Παραγγελίας

        #Ορισμός πεδίων φορμας
        tk.Label(order_window, text="Ημερομηνία Παραγγελίας:").grid(row=0, column=0)
        tk.Label(order_window, text=order_date).grid(row=0, column=1)

        tk.Label(order_window, text="Αριθμός Παραγγελίας:").grid(row=1, column=0)
        tk.Label(order_window, text=order_number).grid(row=1, column=1)

        tk.Label(order_window, text="Όνομα Πελάτη:").grid(row=2, column=0)
        customer_name = tk.Entry(order_window)
        customer_name.grid(row=2, column=1)

        tk.Label(order_window, text="Επώνυμο Πελάτη:").grid(row=3, column=0)
        customer_surname = tk.Entry(order_window)
        customer_surname.grid(row=3, column=1)

        tk.Label(order_window, text="Ημερομηνία Παράδοσης:").grid(row=4, column=0)
        delivery_date = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")
        tk.Label(order_window, text=delivery_date).grid(row=4, column=1)

        tk.Label(order_window, text="Περιγραφή Είδους:").grid(row=5, column=0)
        item_description = tk.Entry(order_window)
        item_description.grid(row=5, column=1)

        tk.Label(order_window, text="Ποσότητα:").grid(row=6, column=0)
        quantity = tk.Entry(order_window)
        quantity.grid(row=6, column=1)

        tk.Label(order_window, text="Τιμή ανά μονάδα:").grid(row=7, column=0)
        unit_price = tk.Entry(order_window)
        unit_price.grid(row=7, column=1)

        tk.Label(order_window, text="ΦΠΑ (%):").grid(row=8, column=0)
        vat_rate = tk.StringVar(order_window)
        vat_rate.set("24")  # Default value
        vat_options = ttk.Combobox(order_window, textvariable=vat_rate, values=["24", "13"])
        vat_options.grid(row=8, column=1)

        #Ορισμος συναρτησεων κεντρικου μενου
        def save_order():
            try:
                name = customer_name.get()
                surname = customer_surname.get()
                item = item_description.get()
                qty = int(quantity.get())
                price = float(unit_price.get())
                vat = float(vat_rate.get())

                if qty <= 0:
                    raise ValueError("Η ποσότητα πρέπει να είναι θετική.")
                if price < 0:
                    raise ValueError("Η τιμή δεν μπορεί να είναι αρνητική.")

                total = qty * price * (1 + vat / 100)
                order = {
                    "Αριθμός": order_number,
                    "Ημερομηνία": order_date,
                    "Όνομα": name,
                    "Επώνυμο": surname,
                    "Ημερομηνία Παράδοσης": delivery_date,
                    "Περιγραφή": item,
                    "Ποσότητα": qty,
                    "Τιμή": price,
                    "ΦΠΑ": vat,
                    "Σύνολο": total
                }

                self.orders.append(order)
                self.save_to_csv(order)
                messagebox.showinfo("Επιτυχία", "Η παραγγελία καταχωρήθηκε επιτυχώς.")
                order_window.destroy()

            except ValueError as e:
                messagebox.showerror("Σφάλμα", str(e))
            except Exception as e:
                messagebox.showerror("Σφάλμα", "Παρουσιάστηκε σφάλμα κατά την αποθήκευση της παραγγελίας.")

        tk.Button(order_window, text="Αποθήκευση", command=save_order).grid(row=9, columnspan=2)
    #Εγγαφη στο αρχειο csv
    def save_to_csv(self, order):
        with open("orders.csv", mode="a", newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=order.keys())
            if file.tell() == 0:
                writer.writeheader()  #Γραψε τα Headers μονο αν το αρχειο ειναι αδειο 
            writer.writerow(order)

    def cancel_order(self):
        order_id = simpledialog.askinteger("Ακύρωση Παραγγελίας", "Εισάγετε τον αριθμό της παραγγελίας προς ακύρωση:")
        if order_id is not None:
            self.orders = [order for order in self.orders if order["Αριθμός"] != order_id]
            self.save_orders_to_csv()
            messagebox.showinfo("Επιτυχία", "Η παραγγελία ακυρώθηκε επιτυχώς.")

    def save_orders_to_csv(self):
        with open("orders.csv", mode="w", newline='', encoding='utf-8') as file:
            if self.orders:
                writer = csv.DictWriter(file, fieldnames=self.orders[0].keys())
                writer.writeheader()
                writer.writerows(self.orders)

    def view_orders(self):
        delivery_date = simpledialog.askstring("Προβολή Παραγγελιών", "Εισάγετε την ημερομηνία παράδοσης (YYYY-MM-DD):")
        if delivery_date:
            filtered_orders = [order for order in self.orders if order["Ημερομηνία Παράδοσης"] == delivery_date]
            if filtered_orders:
                orders_str = "\n".join([f"{o['Αριθμός']}: {o['Περιγραφή']} - {o['Σύνολο']}€" for o in filtered_orders])
                messagebox.showinfo("Παραγγελίες", f"Βρέθηκαν οι παραγγελίες:\n{orders_str}")
            else:
                messagebox.showinfo("Παραγγελίες", "Δεν βρέθηκαν παραγγελίες για την ημερομηνία αυτή.")

    def best_customer(self):
        if not self.orders:
            messagebox.showinfo("Καλύτερος Πελάτης", "Δεν υπάρχουν παραγγελίες.")
            return

        customer_totals = {}
        for order in self.orders:
            full_name = f"{order['Όνομα']} {order['Επώνυμο']}"
            if full_name not in customer_totals:
                customer_totals[full_name] = 0
            customer_totals[full_name] += order["Σύνολο"]

        best_customer = max(customer_totals, key=customer_totals.get)
        max_total = customer_totals[best_customer]
        messagebox.showinfo("Καλύτερος Πελάτης", f"Καλύτερος Πελάτης: {best_customer} με συνολική αξία παραγγελιών {max_total}€.")


#Κληση συναρτησης
if __name__ == "__main__":
    root = tk.Tk()
    app = FurnitureStoreApp(root)
    root.mainloop()