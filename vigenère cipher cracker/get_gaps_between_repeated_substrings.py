CIPHERTEXT = "GEHDRSTAONLLRGYRVWRGWCNBQEOUSRSBUIQIQCCNVBCSA" + \
    "XVWTMVZJHGSARBASZYIRMAPGWWGNAQMGRGSWRMSTIEH" + \
    "KFIENOLHOHPGPYRCLWBODCSCUSUSEURUMQNCLEQJWJCOJ" + \
    "GGWVCWQYFNRRSCACRIPCRYXNJHPIFCOLHQJHYMAVCRMBW"
POSSIBLE_ENCRYPTED_STRINGS = ("olh", )

CIPHERTEXT = CIPHERTEXT.lower()
POSSIBLE_ENCRYPTED_STRINGS = [string.lower() for string in POSSIBLE_ENCRYPTED_STRINGS]

for string in POSSIBLE_ENCRYPTED_STRINGS:
    possible_encrypted_string_indices = list()
    start_i = CIPHERTEXT.find(string)
    while start_i != -1:
        possible_encrypted_string_indices.append(start_i)
        start_i = CIPHERTEXT.find(string, start_i + 1)

    for i in range(len(possible_encrypted_string_indices) - 1):
        print(possible_encrypted_string_indices[i + 1] - possible_encrypted_string_indices[i], end=" ")
    print()