### Made by Carlos Paredes for the course IMT1001 HOMEWORK PUC de Chile
### Licenced by MIT LICENSE 2019

####THIS ALGORITHM IS USED BY THE FORM OF LOCATION(ENCRIPTEDWORD) = LOCATION(ORIGINALWORD) + LOCATION(CORRESPONDENT KEY), THIS WILL BE USED BECAUSE
##IF WE USE THE TABULA RECTA AS A MATRIX WE WILL GET THE SAME RESULT BUT USING MORE RESOURSES TO DO IT

import string
import FrequencyAnalysis  #to remove the non alphabetic characters
global Upperletters
Upperletters = 'abcdefghijklmnopqrstuvwxyz'.upper() ###our alphabet


text_to_encrypt = open('non_encriptedfile_dir.txt','r',encoding='utf-8')
lines_to_encrypt = text_to_encrypt.readlines()
text_to_encrypt.close()
#############################################################################################

def total_key(wordtotal,key):
    keylenght = len(key)
    plain_text_key =''
    for i in range(wordtotal):
        plain_text_key+=key[i%(keylenght)]
    return plain_text_key
def wordcounter(line):
    count = 0
    line = line.upper()
    for word in line:
        if word in Upperletters:
            count+=1
    return count
def vigenere_encrypt(line,cipherkey):  
    full_key = total_key(wordcounter(line),cipherkey)
    encripted_line=''
    line = line.upper()
    o = 0
    for i in range(len(line)):
        if line[i] in Upperletters:
            encripted_line+=Upperletters[(Upperletters.find(line[i])+Upperletters.find(full_key[o]))%(len(Upperletters))]##used the above algorithm
            o+=1 ##a simple counter for the location in full_key string
        else:
            encripted_line+=line[i]
    return encripted_line

def main():
    E_text = open('vigenere_encrypted.txt','w',encoding='utf-8')


    vigenere_cipherkey = input('Enter the cipherkey (strings only): ').upper()


    for line in lines_to_encrypt:
        line = line.replace('\n','')
        encripted_line = vigenere_encrypt(line,vigenere_cipherkey)
        encripted_line+='\n'
        E_text.write(encripted_line)
    E_text.close()

if __name__=='__main__':
    main()