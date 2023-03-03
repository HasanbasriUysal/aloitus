# GET BASIC INFORMATION ABOUT AN ATHLETE AND CREATE ATHLETE OBJECTS
#------------------------------------------------------------------

#LIBRARIES AND MODULES
import kuntoilija

# Enter information about an athlete
nimi =  input("Nimi: ")

#Loop until user gives a correctly formatted value to height question
while True:
    pituus_txt =  input("Pituus (cm): ")

    #Let's try to convert input to numeric
    try:
        pituus = float(pituus_txt)   
        break
    #If an error occurs tell the user to cherck
    except Exception as e:
        print("Virhe syötetyssa arvossa, älä käytä yksiköitä", e)

# Loop until correct wight value
while True:
    paino_txt =  input("Paino (kg): ")

    #Let's try to convert input to numeric
    try:
        paino = float(paino_txt)   
        break
    #If an error occurs tell the user to cherck
    except Exception as e:
        print("Virhe syötetyssa arvossa, älä käytä yksiköitä", e)

# Loop until correct age value
while True:
    ika_txt =  input("Ika: ")

    #Let's try to convert input to numeric
    try:
        ika = float(ika_txt)   
        break
    #If an error occurs tell the user to cherck
    except Exception as e:
        print("Virhe syötetyssa arvossa, älä käytä yksiköitä", e)        

# Loop until correct gender value
while True:
    sukupuoli_txt =  input("Sukupuoli (1 mies), (0 nainen): ")

    #Let's try to convert input to numeric
    try:
        sukupuoli = float(sukupuoli_txt)   
        break
    #If an error occurs tell the user to cherck
    except Exception as e:
        print("Virhe syötetyssa arvossa, vain 1 ja 0 sallittu", e)


kuntoilija1 = kuntoilija.Kuntoilija(nimi, pituus,paino,ika,sukupuoli)

print(kuntoilija1.nimi, "painoindeksisi on ", kuntoilija1.bmi)