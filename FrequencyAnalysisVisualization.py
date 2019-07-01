### Made by Carlos Paredes for the course IMT1001 HOMEWORK PUC de Chile
### Licenced by MIT LICENSE 2019


import numpy as np
import matplotlib.pyplot as plt
import FrequencyAnalysis as freqA

#this script uses numpy and matplotlib to visualizate the data



text_to_analize = open('non_encriptedfile_dir.txt','r',encoding='utf-8')
lines_to_analize = text_to_analize.readlines()
text_to_analize.close()
#############################################################################################
data,total = freqA.frecuency_analisis(lines_to_analize)

Y=[(data[1][i]/total)*100 for i in range(len(data[1]))]
Classes = data[0]
X = np.arange(len(Classes))
plt.bar(X,Y,align='center',alpha=0.5)
plt.xticks(X, Classes)
plt.ylabel('Words (%)')
plt.title('Frequency')

plt.show()
