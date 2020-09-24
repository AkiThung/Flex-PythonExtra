#hier importeer je de os module
import os


# de huidige directory opvragen en opslaan in de  variabele: werkmap
werkmap = os.getcwd()


# de letters cwd staan voor : current working directory


#op het scherm printen
print("de huidige map is: " + werkmap)

# een nieuwe map maken met os.mkdir()
os.mkdir("Een nieuwe map")

#gebruiker om de naam van de map  te vragen

mapnaam = input("welke naam wil je voor deze map? ")

# als de lengte van de mapnaam > 0 is dan maken we de map
lengte_mapnaam = len(mapnaam)
if lengte_mapnaam > 0:
    os.mkdir(mapnaam)
    print("De map " + mapnaam + "is gemaakt. ")
else:
    print("je hebt geen naam ingevoerd")
