#soomin kim
def main():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
    menu_input = input('Please enter an option:')
    password_input = input('Please enter your password to encode:')
    encoded = ''
    if menu_input == '1':
        encoded += encode(password_input)
        print('Your password has been encoded and stored!')
    elif menu_input == '2':
        print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}.")
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