#stap 1 importeer de random library
import random

#stap2 print wat het is
print("Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"

#stap 3 zorg dat er ingevuld kan worden hoeveel verschillende wachtwoorden je wil
nummer = input("Hoeveel wachtwoorden wil je?")
nummer = int(nummer)

#stap 4 zorg dat er ingevuld kan worden hoeveel characters het wachtwoord moet hebben
lengte = input("Hoelang moet je wachtwoord zijn in characters?")
lengte = int(lengte)

#stap 5 print de gegenereerde wachtwoorden
print("\nDit zijn je wachtwoorden:")

for pwd in range(nummer):
  password = ''
  for c in range(lengte):
    password += random.choice(chars)
  print(password)

