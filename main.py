#soomin kim
def main():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
    menu_input = input('Please enter an option:')
    password_input = input('Please enter your password to encode:')
    if menu_input == '1':
        encode(password_input)
        print('Your password has been encoded and stored!')
    elif menu_input == '2':
        pass
    else:
        exit()

def encode(password):
    l = []
    for i in password:
        i += 3
        if i >= 10:
            i = int(str(i)[-1])
            l.append(i)
        else:
            l.append(i)

    encoded = int(''.join(l))
    return encoded

if __name__== '__main__':
    main()