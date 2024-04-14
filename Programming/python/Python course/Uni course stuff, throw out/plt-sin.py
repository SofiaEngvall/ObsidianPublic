#använda linspace() för att generera värden för x-axeln. 

import matplotlib.pyplot as plt 
import numpy as np                         #matematikmodul som innehåller funktionen linspace() och mycket mera


#lägg till en lista med x-koordinater med linspace()-funktionen:
x_values = np.linspace(0,100,100)          #skapar 100 x-värden jämnt fördelade mellan 0 och 100.

#skapa sinus- och cosinuskurvor genom att använda flera plot()-funktioner:
plt.plot(x_values, np.sin(2*3.14*x_values/100), color = 'red', label='Sinuskurva')                      
plt.plot(x_values, np.cos(2*3.14*x_values/100), color = 'blue', linestyle= 'dashed', label='Cosinuskurva') 
                                                                                         
ax = plt.gca()
ax.set_facecolor('lightgreen')

plt.title('Plotta sinus- och cosinuskurvor')
plt.xlabel('Förklarande text för x-axeln hamnar här')
plt.ylabel('Förklarande text för y-axeln hamnar här')      
plt.legend()

plt.grid()

plt.show()
