from caeser_cipher import encrypt, decrypt

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


if direction.lower() == 'encode':
    encoded = encrypt(text, int(shift));
    print(f'The encoded text is {encoded}')
elif direction.lower() == 'decode':
    decoded = decrypt(text, int(shift));
    print(f'The decoded text is {decoded}')
else :
    print("There's only encode option available!!!");
 