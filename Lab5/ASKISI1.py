import math
R = float(input("Πληκτρολογησε την ακτίνα της σφαιρας: "))
Sigma = input("Πληκτρολογησε S για υπολογισμο επιφανειας ή V για τον υπολογισμο του ογκου σφαιρας: ")

def Sfaira(R,Sigma):
    if Sigma == "S" or Sigma=="s":
        Epifaneia=4*math.pi*(R**2)
        return (f"Η επιφανεια της σφαιρας ισουται με: {Epifaneia:.2f}")
    elif Sigma=="V" or Sigma=="v":
        Ogkos=(4/3)*math.pi*(R**3)
        return (f"Ο ογκος της σφαιρας ισουται με: {Ogkos:.2f}")


print("%s" %Sfaira(R,Sigma))