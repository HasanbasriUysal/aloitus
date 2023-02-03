#KUNTOILIJAN TIEDOT OLIO-OHJELMOINTINA
#=====================================

#KIRJASTOT JA MODULIT(LIBRARIES AND MODULES)
#------------------------------------------

import fitness

#LUOKKAMÄÄRITYKSET(CLASS DEFINITIONS)
#------------------------------------

#Kuntoilija-luokka Yliluokka JunioriKuntoilijalle(super class)
class Kuntoilija:
    """Luokka kuntoilijan tietoja varten"""

    #Olionmuodostin eli konstruktori, self ->tuleva olio
    def __init__(self, nimi,pituus,paino,ika,sukupuoli):
        
        #Määritellään tulevan olion ominaisuudet(property), luokan kentät(field)
        self.nimi= nimi
        self.pituus=pituus
        self.paino=paino
        self.ika=ika
        self.sukupuoli=sukupuoli
        self.bmi=fitness.laske_bmi(self.paino,self.pituus)
   

    #Metodi rasvaprosentin laskemiseen(yleinen/aikuinen)
    def rasvaprosentti(self):
        self.rasvaprosentti=fitness.aikuisen_rasvaprosentti(self.bmi,self.ika,self.sukupuoli)
        return self.rasvaprosentti

#---------------------------------------------------------------
#JunioriKuntoilija-luokka Kuntoilija-luokan aliluokka (subclass)
class JunioriKuntoilija(Kuntoilija):
    """Luokka nuoren kuntoilijan tiedoille"""
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):

        #Määritellään priytyminen, mitä ominaisuuksia perili
        super().__init__(nimi, pituus, paino, ika, sukupuoli)

    #Metodi rasvaprosentin laskemiseen(yleinen/aikuinen)
    def rasvaprosentti(self):
        self.rasvaprosentti=fitness.lapsen_rasvaprosentti(self.bmi,self.ika,self.sukupuoli)
        return self.rasvaprosentti


if __name__ == "__main__":

    #Luodaan oli luokasta Kuntoilija 
    kuntoilija=Kuntoilija("Kalle kuntoilija",171,65,40,1)
    print(kuntoilija.nimi,"painaa",kuntoilija.paino,"kg")
#    print("Painoindeksi on",kuntoilija.painoindeksi())
    print("Rasvaprosentti on",kuntoilija.rasvaprosentti())
    

    junioriKuntoilija=JunioriKuntoilija("Aku",171,65,16,1)
    print(junioriKuntoilija.nimi,"painaa",junioriKuntoilija.paino,"kg")
#    print("Painoindeksi on",kuntoilija.painoindeksi())
    print("Rasvaprosentti on",junioriKuntoilija.rasvaprosentti())
