import io


# Bestand in read-only (r) mode openen
bestand2 = open("test.txt", "r")

# Alle tekst lezen met read() en opslaan in de variabele: inhoud
inhoud = bestand2.read()

print("de inhoud van dit bestand is:")
print(inhoud)
 
