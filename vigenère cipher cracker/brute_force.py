from shift_text_backward import shiftBack
from string import ascii_lowercase
from itertools import product

FILENAME = "brute_force_results.txt"
CIPHERTEXT = "GEHDRSTAONLLRGYRVWRGWCNBQEOUSRSBUIQIQCCNVBCSA" + \
    "XVWTMVZJHGSARBASZYIRMAPGWWGNAQMGRGSWRMSTIEH" + \
    "KFIENOLHOHPGPYRCLWBODCSCUSUSEURUMQNCLEQJWJCOJ" + \
    "GGWVCWQYFNRRSCACRIPCRYXNJHPIFCOLHQJHYMAVCRMBW"
CIPHER_LENGTHS = list(range(1, 5))
ALPHABET = ascii_lowercase

CIPHERTEXT = CIPHERTEXT.upper()

with open(FILENAME, "w") as file:
    for cipher_length in CIPHER_LENGTHS:
        for shiftTuple in product(range(len(ALPHABET)), repeat=cipher_length):
            decryptedText = CIPHERTEXT
            for i in range(cipher_length):
                decryptedText = shiftBack(decryptedText, cipher_length, ALPHABET[0], ALPHABET[shiftTuple[i]], i)

            print(decryptedText, file=file)