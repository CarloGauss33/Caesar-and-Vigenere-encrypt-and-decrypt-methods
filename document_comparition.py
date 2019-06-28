### Made by Carlos Paredes for the course IMT1001 HOMEWORK PUC de Chile
### Licenced by MIT LICENSE 2019

####The objetive of this script is to compare ad give how much are similar one to other document
##This is done by the proms of each line

import sys

original_file = open('non_encriptedfile_dir.txt','r')
decrypted_file = open('decryptedFile.txt','r')

def compare(line1,line2):
    pondline = 0
    wrong = []
    for k in range(len(line2)):
        try:
            if line2[k] == line1[k]:
                pondline+=(1/len(line2))
            else:
                wrong.append((line2[k],line1[k]))
        except IndexError:
            pass
            
    return pondline , wrong

originallines = original_file.readlines()
newlines = decrypted_file.readlines()

original_file.close()
decrypted_file.close()
count = 0
docwrong = []
for k in range(len(originallines)):
    try:
       addition, linewrong  = compare(originallines[k],newlines[k])
       count+=addition 
       docwrong.append(linewrong)
    except IndexError:
        pass

print('The score is', (count/len(originallines))*100 )
print('Wrong words are:')
print(linewrong)