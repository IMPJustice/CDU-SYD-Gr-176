from Question2_chapter2 import *
def main():
    def find_shift_key(cryptogram):
        for shift in range(26):
            decrypted = decrypt_cryptogram(cryptogram, shift)
            if "MARILYN MONROE" in decrypted:
                return shift, decrypted

    # Cryptogram solver
    cryptogram = """
    VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VARPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYY QBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR
    """.replace("\n", " ").strip()

    shift, decrypted_quote = find_shift_key(cryptogram)
    print(f"\nShift key: {shift}")
    print(f"Decrypted quote: {decrypted_quote}")
if __name__ == "__main__":
    main()