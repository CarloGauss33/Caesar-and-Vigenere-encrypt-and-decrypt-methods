### Made by Carlos Paredes for the course IMT1001 HOMEWORK PUC de Chile
### Licenced by MIT LICENSE 2019
import string
################ this libraries will be used for data visualization ##############
global Upperletters
Upperletters = 'abcdefghijklmnopqrstuvwxyz'.upper()


#################creating a form to delete non natural words###############################
ascii_chars = string.printable
global non_natural_caracters
non_natural_caracters = []

for letter in ascii_chars:
    if letter not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        non_natural_caracters.append(letter)
############################################################################################
def non_natural_remover(line):
    non_natural = "".join(non_natural_caracters)
    newline = ""    
    for word in line:
        if word not in non_natural:
            newline+=word
    return newline
#########################Creating the frequency analizer#####################################
def frecuency_analisis(text):
    words = [k for k in Upperletters]
    globalcount = 0
    counters = [0 for i in range(len(words))]
    for line in text:
        line.replace(" ","").replace("\n","")
        trated_line = non_natural_remover(line)
        frecuency_analisis
        Distribution_Matrix = []
        line_to_analize = line.upper()
        for k in range(len(Upperletters)):
                wordcount = line_to_analize.count(Upperletters[k])
                counters[k]=counters[k]+wordcount
                globalcount+=wordcount
    Distribution_Matrix.append(words)
    Distribution_Matrix.append(counters)
    return Distribution_Matrix, globalcount
#############################################################################################



