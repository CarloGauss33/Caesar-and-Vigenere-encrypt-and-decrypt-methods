### Made by Carlos Paredes for the course IMT1001 HOMEWORK PUC de Chile
### Licenced by MIT LICENSE 2019
##Almost bruteforce with polinomial complexity O(n * K^2), using Friedman test and Frequency analysis

##########ATACK TYPE ONE. this gives potencial keywords using old methods
######The idea is use Frequency analisys and Dictionary attack to get the best decryption for the vigenere cipher method
###this type of atack gives not nescesary the correct key, but gives one thats make the text more easy to read
import FrequencyAnalysis
import sys
import detectEnglish
from Vigenere_decrypt import vigenere_decrypt
import itertools
import string 

global Upperletters
Upperletters = 'abcdefghijklmnopqrstuvwxyz'.upper()
global english_frequency
english_frequency = (0.0749, 0.0129, 0.0354, 0.0362, 0.1400, 0.0218, 0.0174, 0.0422, 0.0665, 0.0027, 0.0047,0.0357, 0.0339, 0.0674, 0.0737, 0.0243, 0.0026, 0.0614, 0.0695, 0.0985, 0.0300, 0.0116,0.0169, 0.0028, 0.0164, 0.0004)


text_to_analize = open(sys.argv[1],'r',encoding='utf-8')
lines_to_analize = text_to_analize.readlines()
text_to_analize.close()

def mytextfreq(text):
    data,total = FrequencyAnalysis.frecuency_analisis(text)
    aux = [i/total for i in data[1]]
    return aux

def compare(text):
    return sum(abs(freq-English) for freq, English in zip(mytextfreq(text), english_frequency))

def join_lines(lines,quantity):
    newline = ''
    for k in range(quantity):
        newline+=lines[k].replace("\n"," ")
    return newline

def vigenere_attack(text=lines_to_analize, maxkeylenght=5,fragmentsize = 100): ###the result are the posible keys for a n-sized fragment of the text
    text_to_decript=[word for word in join_lines(text,fragmentsize)]
    u = join_lines(text,fragmentsize)
    if type(maxkeylenght)==int:
        possiblekeys = []
        for keylength in range(1,maxkeylenght+1):
            key = [None] * keylength
            for key_index in range(keylength):
                letters = "".join(itertools.islice(text_to_decript, key_index, None, keylength))
                posibleShifts = []
                for key_char in Upperletters:
                    posibleShifts.append((compare(vigenere_decrypt(join_lines(letters,fragmentsize), key_char)), key_char))
                key[key_index] = min(posibleShifts, key=lambda x: x[0])[1]
            possiblekeys.append("".join(key))
        possiblekeys.sort(key=lambda key: compare(vigenere_decrypt(join_lines(text,fragmentsize), key)))
        print(possiblekeys[:2])
        return possiblekeys[:2]
    #elif type(maxkeylenght)==list:
    #   pass ###this is for Kasiski examination

def kasiski_examination(message):
    # Returns a dict with the keys of the sequence and values of a list of spacings (num of letters between the repeats).
    ascii_chars = string.printable
    non_natural_caracters=[]
    for letter in ascii_chars:
        if letter not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            non_natural_caracters.append(letter)
            non_natural_caracters = ''.join(non_natural_caracters)
        # Use a regular expression to remove non-letters from the message.

    message = non_natural_caracters.sub('', message.upper())
    seqSpacings = {} # keys are sequences, values are list of int spacings
    for seqLen in range(3, 6):
        for seqStart in range(len(message) - seqLen):
            # Determine what the sequence is, and store it in seq
            seq = message[seqStart:seqStart + seqLen]

            # Look for this sequence in the rest of the message
            for i in range(seqStart + seqLen, len(message) - seqLen):
                if message[i:i + seqLen] == seq:
                    # Found a repeated sequence.
                    if seq not in seqSpacings:
                        seqSpacings[seq] = [] 

                    # Append the spacing distance between the repeated
                    # sequence and the original sequence.
                    seqSpacings[seq].append(i - seqStart)
    return seqSpacings

def vigenere_final_decription(text=lines_to_analize):
    keys = vigenere_attack()

if __name__=='__main__':
    vigenere_attack()

