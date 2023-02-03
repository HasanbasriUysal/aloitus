#KUNTOILIJAN TIEDOT OLIO-OHJELMOINTINA
#=====================================

#KIRJASTOT JA MODULIT(LIBRARIES AND MODULES)
#------------------------------------------

import fitness

#LUOKKAMÄÄRITYKSET(CLASS DEFINITIONS)
#------------------------------------

class Kuntoilija:
    """Luokka kuntoilijan tietoja varten"""

    #Olionmuodostin eli konstruktori
    def __init__(self, nimi,pituus,paino,ika,sukupuoli):
        
        #Määritellään tulevan olion ominaisuudet(property), luokan kentät(field)
        self.nimi= nimi
        self.pituus=pituus
        self.paino=paino
        self.ika=ika
        self.sukupuoli=sukupuoli
        self.bmi=fitness.laske_bmi(self.paino,self.pituus)

    #Metodi painoindeksin laskemiseen
    def painoindeksi(self):
        self.bmi=fitness.laske_bmi(self.paino,self.pituus)
        return self.bmi

    #Metodi rasvaprosentin laskemiseen(aikuinen)
    def rasvaprosentti(self):
        self.rasvaprosentti=fitness.aikuisen_rasvaprosentti(self.bmi,self.ika,self.sukupuoli)
        return self.rasvaprosentti



if __name__ == "__main__":

    #Luodaan oli luokasta Kuntoilija 
    kuntoilija=Kuntoilija("Kalle kuntoilija",171,65,40,1)
    print(kuntoilija.nimi,"painaa",kuntoilija.paino,"kg")
#    print("Painoindeksi on",kuntoilija.painoindeksi())
    print("Rasvaprosentti on",kuntoilija.rasvaprosentti())
