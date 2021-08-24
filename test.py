#Testingground für Variablen und if abfragen

name = input(('Whats you name?'))
print('Ok, your name is ' + name)

if str(name) == 'Marvin':
    print('Oh, you are my creator!')

age = input(('How old are you?'))
print('You are ' + str(age) + ' years old.')

if int(age) < 18:
    print\
        ('You are not allowed to proceed.')
elif int(age) == 18:
    print\
        ('Ah you are a lucky one, you are allowed to proceed, loading...')
else:
    print\
    ('You are allowed to proceed, loading...')

if int(age) >= 18:
        print('What can i do for you ' + name +'?')

#githubtest

