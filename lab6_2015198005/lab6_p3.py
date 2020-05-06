import sys

# Password Encryption/Decryption Program

# init
password_out = ''
case_changer = ord('a') - ord('A')
encryption_key = (('a', 'm'), ('b', 'h'), ('c', 't'), ('d', 'f'), ('e', 'g'),
                  ('f', 'k'), ('g', 'b'), ('h', 'p'), ('i', 'j'), ('j', 'w'), ('k', 'e'), ('l', 'r'),
                  ('m', 'q'), ('n', 's'), ('o', 'l'), ('p', 'n'), ('q', 'i'), ('r', 'u'), ('s', 'o'),
                  ('t', 'x'), ('u', 'z'), ('v', 'y'), ('w', 'v'), ('x', 'd'), ('y', 'c'), ('z', 'a'),
                  ('#', '!'), ('@', '('), ('%', ')'))       #added new keys

encrypting = True

# get password
password_in = input('Enter password: ')

valid = False           #valid password
has_alph = False        #password has alphablet
has_non_alph = False    #password has not alphabet
has_digit = False       #password has digit

for i in password_in:   #i = each character
    if('a' <= i and i <= 'z') or ('A' <= i and i <= 'Z'):   #has alphabet
        has_alph = True
    if i == '%' or i == '@' or i == '#':        #has non alphabet
        has_non_alph = True
    if '0' <= i and i <= '9':       #has digit
        has_digit = True
if has_alph and has_non_alph and has_digit:     #if all 3, valid
    valid = True

for i in password_in: #if all characters within restriction, valid
    if ('a' <= i and i <= 'z') or ('A' <= i and i <= 'Z') or i == '%' or i == '@' or i == '#':
        valid == True
    else:
        valid == False

if valid == False:      #if invalid password
    print('Invalid password!')
    sys.exit()

# perform encryption / decryption
if encrypting:
    from_index = 0
    to_index = 1
else:
    from_index = 1
    to_index = 0

case_changer = ord('a') - ord('A')

for ch in password_in:
    letter_found = False

    for t in encryption_key:
        if ('a' <= ch and ch <= 'z') and ch == t[from_index]:
            password_out = password_out + t[to_index]
            letter_found = True
        elif ('A' <= ch and ch <= 'Z') and chr(ord(ch) + 32) == t[from_index]:
            password_out = password_out + chr(ord(t[to_index]) - case_changer)
            letter_found = True
        elif (ch == '#' or ch == '@' or ch == '%') and ch == t[from_index]:     #encrypt non-alphabets
            password_out = password_out + t[to_index]
            letter_found = True

    if not letter_found:
        password_out = password_out + ch

# output
if encrypting:
    print('Your encrypted password is:', password_out)
else:
    print('Your decrypted password is:', password_out)

