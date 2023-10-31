#soomin kim
def main(): #written by soomin kim
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        menu_input = input('Please enter an option:')
        if menu_input == '1':
            password_input = input('Please enter your password to encode:')
            encoded = encode(password_input)
            print('Your password has been encoded and stored!')
        elif menu_input == '2':
            decoded = decode(encoded)
            print(f'The encoded password is {encoded}, and the original password is {decoded}.')
        else:
            exit()

def encode(password): #written by soomin kim
    l = []
    for i in password:
        addition = str(int(i) + 3)
        if int(addition) >= 10:
            addition = str(i)[-1]
            l.append(addition)
        else:
            l.append(addition)
    return ''.join(l)

'''
Written by: Case Zumbrum

decode() encodes an integer password by decreasing each integer by 3

Input:
    password (String): password to be encoded, all characters must be integers and there should be 8 digits

Return:
    decoded_password (String): encoded password
'''
def decode(password):
    decoded_password = ''
    for char in password:
        if char == '0':
            decoded_password += str(7)
        elif char == '1':
            decoded_password += str(8)
        elif char == '2':
            decoded_password += str(9)
        else:
            decoded_password += str(int(char)-3)
    return decoded_password


if __name__== '__main__':
    main()