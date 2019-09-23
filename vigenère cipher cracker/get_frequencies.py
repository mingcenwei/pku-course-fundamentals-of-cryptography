from itertools import takewhile, count
from string import ascii_lowercase

CIPHERTEXT = "GEHDRSTAONLLRGYRVWRGWCNBQEOUSRSBUIQIQCCNVBCSA" + \
    "XVWTMVZJHGSARBASZYIRMAPGWWGNAQMGRGSWRMSTIEH" + \
    "KFIENOLHOHPGPYRCLWBODCSCUSUSEURUMQNCLEQJWJCOJ" + \
    "GGWVCWQYFNRRSCACRIPCRYXNJHPIFCOLHQJHYMAVCRMBW"
CIPHER_LENGTH = 5

CIPHERTEXT = CIPHERTEXT.lower()

substrings = [''.join(
    CIPHERTEXT[start_i + j * CIPHER_LENGTH] for j in takewhile(lambda j: start_i + j * CIPHER_LENGTH < len(CIPHERTEXT), count())
    ) for start_i in range(CIPHER_LENGTH)]

frequencyLists = [
    sorted(((l, round(substring.count(l) / len(substring), 3)) for l in ascii_lowercase if substring.count(l) > 0), key=(lambda t: t[1]), reverse=True)
    for substring in substrings]

for list1 in frequencyLists:
    print(list1)