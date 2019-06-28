### Made by Carlos Paredes for the course IMT1001 HOMEWORK PUC de Chile
### Licenced by MIT LICENSE 2019
import sys
import string 


text_to_cipher = open('non_encriptedfile_dir.txt','r') ##First we should open the text to encrypt

global Character_Dict
Character_Dict = string.printable.replace('\t\n\r\x0b\x0c','') ##Use The Printeable ASCII characters to encrypt and decrypt

try:
    originalkey = int(input("Please insert an integer: "))
except ValueError or TypeError:
    print('INTEGER!!!!, Killing Program')
    sys.exit()


###################################DEFINING ENCRIPTING FUNCTION###############################################
def encript_word(key,word):
    list_dict = []
    
    for i in Character_Dict:
        list_dict.append(i)
    shape = len(list_dict)
    location = Character_Dict.find(word)
    
    if (key+location) <= (shape-1):
        newword = list_dict[key+location]
    else:
        n_position = (key+location) % (shape)
        newword = list_dict[n_position]
    return newword
###############################################################################################################
non_encriptedlines = text_to_cipher.readlines()

text_to_cipher.close()

cipher_text = open('encriptedfile.txt','w')

Cipher_key = originalkey % 26
for line in non_encriptedlines:
    encripted_line = ''
    for word in line[0:len(line)-1]:
        encripted_line+=encript_word(Cipher_key,word)
    encripted_line+=' \n'
    cipher_text.write(encripted_line)

cipher_text.close()
