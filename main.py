import random

little_alpha = 'abcdefghijklmnopqrstuvwxyz'
big_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sym = '~!@#$%^&*()_-+={}[]\|:;"<>,.?/'
num = '0123456789'

time_pas = ''
site = input('What site password? ')
login = input('Enter login: ')

for _ in range(5):
    time_pas += little_alpha[random.randint(0, len(little_alpha) - 1)]
    time_pas += big_alpha[random.randint(0, len(big_alpha) - 1)]
    time_pas += sym[random.randint(0, len(sym)) - 1]
    time_pas += num[random.randint(0, len(num) - 1)]
password_ready = random.sample(time_pas, len(time_pas))
print(''.join(password_ready))
with open('pss.txt', 'a') as password:
    password.write(site + ':\n')
    password.write(login + '\n')
    password.write(''.join(password_ready) + '\n' + '\n')
    print('Password created')







