#FITNESS-MODULIN TESTIT
#======================

#KIRJASTOJEN JA MODULIEN LATAUKSET
import fitness

def test_laske_bmi():
    assert fitness.laske_bmi(64.7,170)==22.4
    assert fitness.laske_bmi(40,170)==13.8
    assert fitness.laske_bmi(100,170)==34.6
    