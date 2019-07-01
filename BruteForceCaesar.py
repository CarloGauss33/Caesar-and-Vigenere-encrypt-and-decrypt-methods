### Made by Carlos Paredes for the course IMT1001 HOMEWORK PUC de Chile
### Licenced by MIT LICENSE 2019
import sys
import string 
import detectEnglish



text_to_decipher = open('encriptedfile.txt','r') ##First we should open the text to decrypt

global Character_Dict
Character_Dict = string.printable.replace('\t\n\r\x0b\x0c','').replace("\\","") ##Use The Printeable ASCII characters to encrypt and decrypt

###################################################################################
def decript_word(key,word):
    list_dict = []
    
    for i in Character_Dict:
        list_dict.append(i)

    shape = len(list_dict)
    location = Character_Dict.find(word)
    
    if (location-key) >= (0):
        newword = list_dict[location-key]
    else:
        n_positioninverse = (location-key)*-1 % (shape)
        n_position = shape - n_positioninverse
        newword = list_dict[n_position]
    return newword
##################################################################################

encripted_lines = text_to_decipher.readlines()

text_to_decipher.close()

cipher_text = open('decryptedFile.txt','w')

for key in range(26):
    decrypted_line = ''
    for word in encripted_lines[0].replace("\n",""):
        decrypted_line+=decript_word(key,word)               

    if detectEnglish.isEnglish(decrypted_line):
        decrypted_line+=' \n'
        cipher_text.write(decrypted_line.replace(decrypted_line[-3],""))  
        for line in encripted_lines[1:len(encripted_lines)-1]:
            decrypted_line = ''
            for word in line[0:len(line)-1]:
                decrypted_line+=decript_word(key,word)
            decrypted_line+=' \n'           
            cipher_text.write(decrypted_line.replace(decrypted_line[-3],""))

    else:
        pass
cipher_text.close()