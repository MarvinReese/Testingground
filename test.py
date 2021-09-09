#Testingground für Variablen und If abfragen

player_name = input ('Whats you name? ')
print('Ok, your name is ' + player_name)

if str(player_name) == 'Marvin':
    print('Oh, you are my creator!')

age = input('How old are you? ')
print('You are ' + str(age) + ' years old.')

if int(age) < 18:
    print\
        ('You are not allowed to proceed.')
    exit()

elif int(age) == 18:
    print\
        ('Ah you are a lucky one, you are allowed to proceed, loading...')

else:
    print\
        ('You are allowed to proceed, loading...')

if int(age) >= 18:
        print('Ok ' + player_name + ' its time to choose your companions!')

#Testingground für Listen

first_companion_name = input("What is the name of your first companion? ")
print("Ok " + first_companion_name + " is on your side")

second_companion_name = input("What is the name of your second companion? ")
print("Ok " + second_companion_name + " is on your side")

companions = [first_companion_name, second_companion_name]
print (companions)

print("Press Enter to continue")
input()

