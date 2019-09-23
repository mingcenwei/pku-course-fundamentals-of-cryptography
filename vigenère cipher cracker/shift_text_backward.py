from itertools import product

def shiftBack(ciphertext, step, plain_char, cipher_char, start_i):
    shift = (ord(cipher_char.lower()) - ord(plain_char.lower())) % 26

    decryptedText = ""
    for i in range(len(ciphertext)):
        if (i - start_i) % step == 0:
            o1 = ord(ciphertext[i].lower()) - shift
            char = chr(o1) if o1 >= ord("a") else chr(o1 + 26)
            decryptedText += char
        else:
            decryptedText += ciphertext[i]

    return decryptedText

if __name__ == "__main__":
    FILENAME = "brute_force_results.txt"
    CIPHERTEXT = "GEHDRSTAONLLRGYRVWRGWCNBQEOUSRSBUIQIQCCNVBCSA" + \
    "XVWTMVZJHGSARBASZYIRMAPGWWGNAQMGRGSWRMSTIEH" + \
    "KFIENOLHOHPGPYRCLWBODCSCUSUSEURUMQNCLEQJWJCOJ" + \
    "GGWVCWQYFNRRSCACRIPCRYXNJHPIFCOLHQJHYMAVCRMBW"
    CIPHER_LENGTH = 5
    # FIRST_N_TO_TRY = 4
    FIRST_N_TO_TRY = 2
    # MOST_COMMON_LETTERS = ("e", "t", "a", "i")
    MOST_COMMON_LETTERS = ("e", )
    FREQUENCY_LISTS = [
        [('s', 0.194), ('i', 0.139), ('m', 0.139), ('w', 0.139), ('e', 0.056), ('h', 0.056), ('v', 0.056), ('x', 0.056), ('c', 0.028), ('g', 0.028), ('l', 0.028), ('p', 0.028), ('r', 0.028), ('y', 0.028)],
        [('b', 0.111), ('e', 0.111), ('q', 0.111), ('a', 0.083), ('c', 0.083), ('o', 0.083), ('v', 0.083), ('f', 0.056), ('g', 0.056), ('z', 0.056), ('l', 0.028), ('n', 0.028), ('p', 0.028), ('r', 0.028), ('t', 0.028), ('y', 0.028)],
        [('c', 0.139), ('j', 0.139), ('n', 0.139), ('r', 0.111), ('u', 0.111), ('h', 0.083), ('w', 0.083), ('a', 0.056), ('m', 0.028), ('o', 0.028), ('p', 0.028), ('v', 0.028), ('y', 0.028)],
        [('c', 0.143), ('g', 0.114), ('r', 0.114), ('s', 0.114), ('h', 0.086), ('o', 0.086), ('b', 0.057), ('d', 0.057), ('i', 0.057), ('w', 0.057), ('a', 0.029), ('k', 0.029), ('p', 0.029), ('t', 0.029)],
        [('r', 0.171), ('g', 0.114), ('l', 0.114), ('q', 0.114), ('y', 0.086), ('a', 0.057), ('n', 0.057), ('u', 0.057), ('c', 0.029), ('f', 0.029), ('j', 0.029), ('m', 0.029), ('p', 0.029), ('s', 0.029), ('t', 0.029), ('w', 0.029)]]

    CIPHERTEXT = CIPHERTEXT.upper()

    with open(FILENAME, "w") as file:
        # for indexTuple in product(range(FIRST_N_TO_TRY), repeat=CIPHER_LENGTH):
        ranges = [range(len(l)) for l in FREQUENCY_LISTS]
        for indexTuple in product(*ranges):
            for indexTuple2 in product(MOST_COMMON_LETTERS, repeat=CIPHER_LENGTH):
                decryptedText = CIPHERTEXT
                for i in range(CIPHER_LENGTH):
                    decryptedText = shiftBack(decryptedText, CIPHER_LENGTH, indexTuple2[i], FREQUENCY_LISTS[i][indexTuple[i]][0], i)

                print(decryptedText, file=file)