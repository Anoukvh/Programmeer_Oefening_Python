#stap 1 importeer de juiste library
import os

#stap 2 maak een while statement waarin je het ip adres kan invullen
while True:

    print('\nTyp het ipadres een gedeelte per keer\ntyp het eerste gedeelte: ', end='')
    ip_adres1 = int(input())
    print('typ het tweede gedeelte: ', end='')
    ip_adres2 = int(input())
    print('typ het derde gedeelte: ', end='')
    ip_adres3 = int(input())
    print('typ het vierde gedeelte: ', end='')
    ip_adres4 = int(input())

#stap 3 voeg de ingevulde getallen samen
    ip_adres = (str(ip_adres1) + '.' + str(ip_adres2) + '.' + str(ip_adres3) + '.' + str(ip_adres4))
    print(ip_adres)
    os.system('ping {}'.format(ip_adres))
    
#stap 4 vraag of je het nog een keer wil invullen of type nee als je het wilt stoppen
    print('\nWil je doorgaan? ', end='')
    antwoord = str(input())
    if antwoord == 'nee':
        break
