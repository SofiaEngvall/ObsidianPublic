#Function to read data from csv file to two dimensional list
def read_file(filename):
    file = open(filename, 'r', encoding = 'utf-8-sig')
    data = []

    for line in file:
        line = line.replace('\n','')
        split_line = line.split(';')
        data.append(split_line)
    return data

#Function to return a list of elements staring with request
def get_data(table, request):
    for line in table:
        if(line[0]==request): return line
    return "Requested data not found"

#Retrieve data from files
kpiData = read_file('kpi-1.csv')
tjansteData = read_file('tjänster-1.csv')
livsmedelData = read_file('livsmedel-1.csv')

#Output selected portion of retrieved data
print('KPI')
print(kpiData[0])
print(get_data(kpiData,'2022'))

print('Tjänster')
print(tjansteData[0])
print(get_data(tjansteData,'livsmedel och alkoholfria drycker'))

print('Livsmedel')
print(livsmedelData[0])
print(get_data(livsmedelData,'bröd och övriga spannmålsprodukter'))

#------------

import matplotlib.pyplot as plt

years = range(1980, 2023)
months = ('Januari', 'Februari', 'Mars', 'Maj', 'Juni', 'Juli', 'Augusti', 'September', 'Oktober', 'November', 'December')
print(len(months))

#Returns list of the median for all years
def get_medians(lists):
    medians = []
    for year in lists:
        msum = 0
        for value in year[1:]:
            msum += float(value)
        medians.insert(0,msum/len(year))
    return medians

#Returns a list with values for the selected month for all years
def get_month_values(month):
    values = 1
    return values

#Ask for month to compare to
month = input('Välj månad att jämföra med (1-12): ')

#Get medians and make bar graph and plot line for it
medians = get_medians(kpiData)
plt.bar(x, medians, color='lightblue', label='Medel KPI')
plt.plot(x, medians, color='blue', label='Medel KPI Linje')

#Get month values and  plot line for it
month_values = get_month_values()
plt.plot(x, month_values, color='red', label=months[month-1])

#Add descriptive information and show the diagram
plt.title('Konsumentprisindex År 1980-2022')
plt.xlabel('År')
plt.ylabel('Konsumentprisindex')
plt.ylim(100,400)
plt.xlim(1980,2023)
plt.grid()
plt.show()


