from itertools import takewhile, count
from string import ascii_lowercase

CIPHERTEXT = "GEHDRSTAONLLRGYRVWRGWCNBQEOUSRSBUIQIQCCNVBCSA" + \
    "XVWTMVZJHGSARBASZYIRMAPGWWGNAQMGRGSWRMSTIEH" + \
    "KFIENOLHOHPGPYRCLWBODCSCUSUSEURUMQNCLEQJWJCOJ" + \
    "GGWVCWQYFNRRSCACRIPCRYXNJHPIFCOLHQJHYMAVCRMBW"
MAX_CIPHER_LENGTH = 10

CIPHERTEXT = CIPHERTEXT.lower()

for cipherLength in range(1, MAX_CIPHER_LENGTH + 1):
    substrings = [''.join(
        CIPHERTEXT[start_i + j * cipherLength] for j in takewhile(lambda j: start_i + j * cipherLength < len(CIPHERTEXT), count())
        ) for start_i in range(cipherLength)]
    sumsOfSquaredFrequencies = [round(sum(
        substring.count(letter) ** 2 for letter in ascii_lowercase
        ) / (len(substring) ** 2), 3) for substring in substrings]
    print(sumsOfSquaredFrequencies)