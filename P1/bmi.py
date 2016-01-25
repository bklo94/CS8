#bmi.py
#Brandon Lo, 4/14/15

def bmi(height, weight):
    kg = weight/2.20462262
    m = height/39.3700787
    bmi = kg/(m**2)
    return bmi

def category(bodyMassIndex):
    if bodyMassIndex <= 18.5:
        return 'Underweight'
    elif bodyMassIndex <= 25 and bodyMassIndex > 18.5:
        return 'Normal'
    elif bodyMassIndex <= 30 and bodyMassIndex > 25:
        return 'Overweight'
    else:
        return 'Obese'








# solution must be above this comment

# do not change any part of the code below
def main():
    height = float( input("enter height in inches: ") )
    weight = float( input("enter weight in pounds: ") )
    bodyMassIndex = bmi(height, weight)
    bmiCat = category(bodyMassIndex)
    allCats = ['Underweight','Normal','Overweight','Obese']
    if bmiCat in allCats:
        print("BMI is {0:.1f}: {1}".format(bodyMassIndex, bmiCat))
    else: print ("Category error:",bmiCat,'\n  must be one of ',allCats)

main()
