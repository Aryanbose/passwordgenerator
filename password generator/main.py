import random 

print ('This is your password generator! ')


chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$%^&*()'
number = input('Amount of passwords to generate: ')
number=int(number)
length = input('Your pass length: ')
length = int(length)
print('here are your passwords')
for pwd in range(number):
    passwords=''
    for c in range(length):
        passwords+=random.choice(chars)
    print(passwords)


