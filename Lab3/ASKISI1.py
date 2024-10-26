
Thermokrasia=int(input('Πληκτρολόγησε την επιθυμητή θερμοκρασία: '))
Klimaka=input('Πληκτρολογησε F για θερμακρασια σε κλιμακα Fahrenheit ή C για θερμοκρασια σε κλίμακα Celcious: ')
klimaka2=Klimaka

if klimaka2=="F":
    Metatropi=(9/5)*Thermokrasia+32
    print(f"{Thermokrasia} στην κλίμακα Fahrenheit ισούται με {Metatropi} βαθμούς στην κλίμακα Celsious")
elif klimaka2=="C":
    Metatropi=(5/9)*Thermokrasia-32
    print(f"{Thermokrasia} στην κλίμακα Celsious ισούται με {Metatropi} βαθμούς στην κλίμακα Fahreneit")
else:
    print("Πρέπει να επιλέξεις την κλίμακα F ή C")