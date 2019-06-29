### Made by Carlos Paredes for the course IMT1001 HOMEWORK PUC de Chile
### Licenced by MIT LICENSE 2019
import string

import numpy as np  
import matplotlib.pyplot as plt
################ this libraries will be used for data visualization ##############
global lowerletters
lowerletters = 'abcdefghijklmnopqrstuvwxyz'


#################creating a form to delete non natural words###############################
ascii_chars = string.printable
global non_natural_caracters
non_natural_caracters = []

for letter in ascii_chars:
    if letter not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        non_natural_caracters.append(letter)
print(non_natural_caracters)
############################################################################################
def non_natural_remover(line):
    non_natural = "".join(non_natural_caracters)
    newline = ""
    for word in line:
        if word not in non_natural:
            newline+=word
    return newline
#########################Creating the frequency analizer#####################################
def frecuency_analisis(lines):
    Distribution_Matrix = []
    globalcount = 0
    line_to_analize = line.lower()
    words = []
    counters = []
    for word in lowerletters:
        wordcount = lowerletters.count(word)
        words.append(word)
        counters.append(wordcount)
        globalcount+=wordcount
    Distribution_Matrix.append(words).append(counters)
    return Distribution_Matrix, globalcount
#############################################################################################
text_to_analize = open('non_encripted_file_dir.txt','r')
lines_to_analize = text_to_analize.readlines()
text_to_analize.close()
############################################################################################
total_letters = 0
for line in lines_to_analize:
    line.replace(" ","").replace("\n","")
    trated_line = non_natural_remover(line)
    frecuency_analisis

