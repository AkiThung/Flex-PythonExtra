from PIL import Image, ImageFont, ImageDraw
lettertype = ImageFont.truetype("impact.ttf", 80)

# Afbeelding openen en oplsaan in de variabele met de naam: afbeelding
achtergrond = Image.open("stonks.png")

# De afbeelding tonen in de standaard image viewer van jouw systeem
achtergrond.show()

# De breedte en hoogte van de afbeelding lezen en tonen 
breedte = achtergrond.width
hoogte = achtergrond.height

# Afmetingen op het scherm zetten
# Met str() zet je een int (getal) naar een string om. Dan kan print() het gebruiken.
print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")

# Andere info uitlezen en tonen
print(achtergrond.format, achtergrond.size, achtergrond.mode)

tekengebied = ImageDraw.Draw(achtergrond)

tekst = "When u buy GTA money so u now have \n$9 million instead of $20!"

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype) 
print("tekst_breedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))

tekst_x = (breedte - tekst_breedte) / 2
tekst_y = (hoogte - tekst_hoogte) / 2

tekengebied.multiline_text((tekst_x-2, tekst_y-2), tekst, font=lettertype, fill=(255,255,255))

achtergrond.show()

achtergrond.save("meme_met_tekst.jpg")
