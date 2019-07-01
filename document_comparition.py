### Made by Carlos Paredes for the course IMT1001 HOMEWORK PUC de Chile
### Licenced by MIT LICENSE 2019

####The objetive of this script is to compare ad give how much are similar one to other document
##This is done by the proms of each line

import sys

try:
    original_file = open(sys.argv[1],'r')
    decrypted_file = open(sys.argv[2],'r')
except IndexError:
    print('USE: PY_EXECUTABLE -OriginalDocument -TestDocument')
    sys.exit()

    
def compare(line1,line2):
    pondline = 0
    wrong = []
    for k in range(len(line2)):
        try:
            if line2[k].upper() == line1[k].upper():
                pondline+=(1/len(line2))
            else:
                wrong.append((line2[k],line1[k]))
        except IndexError:
            pass
            
    return pondline , wrong

def main():
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
    return True
if __name__=='__main__':
    main()