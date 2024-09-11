import string

def separate_string(s):
    numbers = ''.join(filter(str.isdigit, s))
    letters = ''.join(filter(str.isalpha, s))
    return numbers, letters

def even_numbers_to_ascii(numbers):
    return [ord(str(int(n))) for n in numbers if int(n) % 2 == 0]

def uppercase_to_ascii(letters):
    return [ord(l) for l in letters if l.isupper()]

def decrypt_cryptogram(cryptogram, shift):
    alphabet = string.ascii_uppercase
    decrypted = ''
    for char in cryptogram:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index - shift) % 26
            decrypted += alphabet[new_index]
        else:
            decrypted += char
    return decrypted

def find_shift_key(cryptogram):
    for shift in range(26):
        decrypted = decrypt_cryptogram(cryptogram, shift)
        if "MARILYN MONROE" in decrypted:
            return shift, decrypted

# Part 1: String manipulation and ASCII conversion
input_string = '56aAww1984sktr235270aYmn145ss785fsq31D0'
numbers, letters = separate_string(input_string)

print("Number string:", numbers)
print("Letter string:", letters)

even_numbers_ascii = even_numbers_to_ascii(numbers)
print("ASCII values of even numbers:", even_numbers_ascii)

uppercase_ascii = uppercase_to_ascii(letters)
print("ASCII values of uppercase letters:", uppercase_ascii)

# Part 2: Cryptogram solver
cryptogram = """
VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VARPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY
NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR
""".replace("\n", " ").strip()

shift, decrypted_quote = find_shift_key(cryptogram)
print(f"\nShift key: {shift}")
print(f"Decrypted quote: {decrypted_quote}")