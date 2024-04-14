# pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np

# dataset
height = [155, 168, 173, 160]
grade = [5, 3, 2, 4]
students = ['Lisa', 'Carl', 'Joe', 'Ella']
pos = range(len(height))

# plot graphs
plt.bar(pos, height)
plt.bar(pos, grade, bottom = height)
plt.plot(pos, height, color = 'red', label='Height')
plt.plot(pos, grade, color = 'purple', label='Grade', linestyle='dashed')

# replace axis label
plt.xticks(pos, students)

plt.title('My Graph')

plt.xlabel('Students')
plt.ylabel('Student Height')

#plt.xlim(0,5)
plt.ylim(0,200)

plt.legend()
plt.gca().set_facecolor('lightblue')
plt.grid()

plt.tight_layout()
plt.show()

