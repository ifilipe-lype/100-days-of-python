alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text: str, shift: int) -> str :
    text_encrypted = "";

    for char in text:
        if char in alphabet:
            letter_index = alphabet.index(char)
            tmp_index = letter_index + shift

            shifted_index = (tmp_index % 25) - 1 if tmp_index > 25  else tmp_index
            letter_after_shift = alphabet[shifted_index]

            text_encrypted += letter_after_shift.upper() if char.isupper() else letter_after_shift
        else:
            text_encrypted += char

    
    return text_encrypted

def decrypt(text: str, shift: int) -> str :
    text_encrypted = "";

    for char in text:
        if char in alphabet:
            letter_index = alphabet.index(char)
            tmp_index = letter_index - shift

            shifted_index = (25 - abs(tmp_index) + 1) if tmp_index < 0  else tmp_index
            letter_after_shift = alphabet[shifted_index]

            text_encrypted += letter_after_shift.upper() if char.isupper() else letter_after_shift
        else:
            text_encrypted += char

    
    return text_encrypted
