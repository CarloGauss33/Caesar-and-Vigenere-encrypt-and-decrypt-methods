### Made by Carlos Paredes for the course IMT1001 HOMEWORK PUC de Chile
### Licenced by MIT LICENSE 2019

####THIS ALGORITHM IS USED BY THE FORM OF  LOCATION(ENCRIPTEDWORD) - LOCATION(Key)= LOCATION(DECRYPTEDWORD)

import string
from Vigenere_cypher import total_key,wordcounter
global Upperletters
Upperletters = 'abcdefghijklmnopqrstuvwxyz'.upper() ###our alphabet

def vigenere_decrypt(encriptedline,cipherkey):
    encriptedline = encriptedline.upper()
    cipherkey = cipherkey.upper()  
    full_key = total_key(wordcounter(encriptedline),cipherkey)
    decripted_line=''
    o = 0
    for i in range(len(encriptedline)):
        if encriptedline[i] in Upperletters:
            decripted_line+=Upperletters[(Upperletters.find(encriptedline[i])-Upperletters.find(full_key[o]))%(len(Upperletters))]##used the above algorithm
            o+=1 ##a simple counter for the location in full_key string
        else:
            decripted_line+=encriptedline[i]
    return decripted_line

def main():
    key = input('Enter the Cipher Key: ').upper()
    encrypted_text=open('vigenere_encrypted.txt','r',encoding='utf-8')
    lines = encrypted_text.readlines()
    encrypted_text.close()
    newtext = open('Vigenere_decrypted_withKey.txt','w',encoding='utf-8')
    for line in lines:
        newtext.write(vigenere_decrypt(line,key))
    newtext.close()

if __name__=='__main__':
    main()
