#Task One Grab the google drive link from .csv File 
import  csv
f = open('find_the_link.csv',encoding = 'utf-8')
csv_data = csv.reader(f)
data = list(csv_data)
#print(data[2])
link_str =''
for row_num,data in enumerate(data):
    link_str += data[row_num]