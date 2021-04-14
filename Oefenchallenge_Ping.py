#stap 1 importeer de juiste library
import os
import string

#stap 2 laat zien welke eisen er zijn verbonden aan het invullen van het ip adres
print("Bij het invullen van de gedeeltes vul je ALLEEN getallen in, letters zullen niet werken!")


#stap 3 maak een while loop waarin je het ip adres kan invullen en het meteen op getallen en cijfers controleerd
while True:
    print('\nTyp het ipadres een gedeelte per keer\ntyp het eerste gedeelte: ', end='')
    ip_adress1 = input()
    if ip_adress1.strip().isdigit():
        break
    else:
        print("Het moet een cijfer zijn wat je invuld")
        
while True:
    print('typ het tweede gedeelte: ', end='')
    ip_adress2 = input()
    if ip_adress2.strip().isdigit():
        break
    else:
        print("Het moet een cijfer zijn wat je invuld")

while True:
    print('typ het derde gedeelte: ', end='')
    ip_adress3 = input()
    if ip_adress3.strip().isdigit():
        break
    else:
        print("Het moet een cijfer zijn wat je invuld")

while True:
    print('typ het vierde gedeelte: ', end='')
    ip_adress4 = input()
    if ip_adress4.strip().isdigit():
        break
    else:
        print("Het moet een cijfer zijn wat je invuld")


#stap 4 voeg de ingevulde getallen samen
ip_adress = (str(ip_adress1) + '.' + str(ip_adress2) + '.' + str(ip_adress3) + '.' + str(ip_adress4))
print(ip_adress)
os.system('ping {}'.format(ip_adress))
    
#stap 5 vraag of je het nog een keer wil invullen of type nee als je het wilt stoppen
print('\nWil je doorgaan? ', end='')
antwoord = str(input())
if antwoord == 'nee':
    exit()
