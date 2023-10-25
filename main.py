def main():
    print('1. encoder\n 2.decoder \n3. exit')
    password_input = input('enter password')
    menu_input = input('enter menu number')
    if menu_input == '1':
        print(encoder(password_input))
    elif menu_input == '2':
        print(decoder(password_input))
    else:
        exit()

def encoder(password):
    l = []
    for i in password:
        l.append(i+3)
    encoded = int(''.join(l))
    return encoded

def decoder(password)
    l = []
    for i in password:
        l.append(i-3)
    encoded = int(''.join(l))
    return encoded

if __name__== '__main__':
    main()