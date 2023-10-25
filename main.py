#soomin kim
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


"""
Written by: Case Zumbrum

decoder decodes a password by decreasing all integers in it by 3

Input:
password (String): Encoded password, must be all integers and should be 8 characters long

Output:
decoded_password (String): Password decoded by reducing all integers by 3
"""
def decoder(password):
    decoded_password = ''
    for char in password:
        decoded_password += str(int(char) - 3)
    return decoded_password

if __name__== '__main__':
    main()