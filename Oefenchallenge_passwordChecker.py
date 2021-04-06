#stap 1 print de voorwaarden van het wachtwoord

print("voorwaarden:")

print("Minstens 1 letter tussen de [a-z] en 1 letter tussen de [A-Z].")
print("Minstens 1 nummer tussen de [0-9].")
print("Minstens 1 character [$#@!%].")
print("Minimale lengte 6 characters.") 
print("Maximale lengte 16 characters.") 

#stap 2 zorg dat de code door een checker heen gaat met if en else en werk met true or false

import re
p = input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@!%]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")
