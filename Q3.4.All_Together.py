# 1. Fixing the for loop to reveal the key
total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total += i - j
print(f"Total after loop: {total}")  # Key revealed


# 2. Decryption Function
def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text


# The encrypted code is available
key = 21  # Key found from part 1
encrypted_code = '''tybony_inenvoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inenvoyr
    ybpny_inenvoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inenvoyr > 0:
        vs ybpny_inenvoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inenvoyr)
        ybpny_inenvoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inenvoyr = 10
    zl_qvpg['xrl4'] = ybpny_inenvoyr - ybpny_inenvoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inenvoyr
    tybony_inenvoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanell!")

cevag(tybony_inenvoyr)
cevag(zl_qvpg)
cevag(zl_frg'''
decrypted_code = decrypt(encrypted_code, key)
print(decrypted_code)

# 3. Correcting errors in the while loop
counter = 0
total = 0  # Initialize total

# Loop until the counter reaches 5
while counter < 5:
    if total < 13:
        total += 1  # Increase total if less than 13
    elif total > 13:
        total -= 1  # Decrease total if greater than 13
    else:
        counter += 2  # Increase counter by 2 only when total equals 13
    print(f"Total: {total}, Counter:{counter}")
 