from datetime import date
import sys

myAge=int(sys.argv[1])

def computeMyBirthDate(age):
    birthdate = date.today().year - age
    return  birthdate

print("Hello you :D")
print(computeMyBirthDate(myAge))
