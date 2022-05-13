import string


def cryptageCesar(x, k):
    return (x+k)


def decryptageCesar(x, k):
    return (x-k)


def cryptage(sentence, key):
    sentencesCrypted = []
    asci = []
    tmp_key = key
    for letter in sentence:
        asci.append(ord(letter))
    for x in asci:
        if x == 32:
            value = 32
        else:
            asciBeta = x-65
            asciCrypted = cryptageCesar(asciBeta, tmp_key)
            value = asciCrypted+65
        sentencesCrypted.append(chr(value))
        tmp_key += 1
    sentencesCrypted = "".join(sentencesCrypted)
    return sentencesCrypted


def decryptage(sentence, k):
    sentenceDecrypted = []
    asci = []
    tmp_key = k
    for letter in sentence:
        asci.append(ord(letter))
    for y in asci:
        if y == 32:
            value = 32
        else:
            numberCrypted = y-65
            numberDecrypted = decryptageCesar(numberCrypted, tmp_key)
            value = numberDecrypted+65
        sentenceDecrypted.append(chr(value))
        tmp_key += 1
    sentenceDecrypted = "".join(sentenceDecrypted)
    return sentenceDecrypted


def decrypt_match_rotor(sentence, rotor):
    alphabet, list_index = [], []
    result = ""
    for l in string.ascii_uppercase.split()[0]:
        alphabet.append(l)

    for chrs in sentence:
        list_index.append(rotor.index(chrs))

    for indx in list_index:
        result += alphabet[indx]

    return result


def match_rotor(sentence, rotor):
    alphabet, list_index = [], []
    result = ""
    for l in string.ascii_uppercase.split()[0]:
        alphabet.append(l)

    for chrs in sentence:
        list_index.append(alphabet.index(chrs))

    for indx in list_index:
        result += rotor[indx]

    return result


def enigma(sentence, key, rotor_list):
    cesar = cryptage(sentence, key)
    for rotor in rotor_list:
        cesar = match_rotor(cesar, rotor)
    print(cesar)


def decrypt_enigma(sentence, key, rotor_liste):
    snc = sentence
    for rotor in rotor_liste:
        snc = decrypt_match_rotor(snc, rotor)

    cesar = decryptage(snc, key)
    print(cesar)


operation = input()
pseudo_random_number = int(input())
liste_rotor = []
for i in range(3):
    rotor = input()
    liste_rotor.append(rotor)


message = input()


if(operation == "ENCODE"):
    enigma(message, pseudo_random_number, liste_rotor)
else:
    decrypt_enigma(message, pseudo_random_number, liste_rotor[::-1])
