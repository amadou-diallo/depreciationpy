#Depreciation by Amadou

import locale

result = locale.setlocale(locale.LC_ALL, '')
if result == "C" or result.startswith("C/"):
    locale.setlocale(locale.LC_ALL,'en_US')
    print("Welcome to the Depreciation Calculator")
    print()
    choice = input("Do you have an Asset? (Y/N): ")
while choice.lower() == "yes":
    doDepreciation()
    
    choice = input("Do you have another Asset? (Y/N): ")
    print()

    print("Thanks for using the Depreciation Calculator!")
        

def getValue(prompt, ntype):
    goodVal = False
    while not goodVal:
        try:
            if ntype.lower == "i":
                v = int(input(prompt))
            else:
                v = float(input(prompt))
                goodVal = True
        except ValueError as ex:
            print("Illegal value: " + str(ex))
            goodVal = False
    return v

def doDepreciation():

    Cost = getValue("Asset Cost: ", "f")
    Salvage = getValue("Salvage Value: ", "f")
    Life = getValue("Life: ", "i")

    totVal = (Cost * Salvage * Life)
    print(str(totVal))

            
            
   

   
