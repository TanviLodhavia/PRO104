from ast import Str
import csv
from collections import Counter
from statistics import median

#new_data="Tanvi L"
#data=Counter(new_data)
#print(data)

#Reading data
with open('filedata.csv', newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
new_data=[]
for i in range(len (file_data)):
    n_num=file_data[i][2]
    new_data.append(float(n_num))

#Mean
n=len(new_data)
total=0
for x in new_data:
    total+=x
mean=total/n
print("Mean is " + str (mean))

#Median
new_data.sort()
if n%2==0:
    median1=float(new_data[n//2])
    median2=float(new_data[n//2-1])
    median=(median1+median2)/2
else:
    median=new_data[n//2]
print(n)
print("Median is " + str(median))

#Mode
data=Counter(new_data)
mode_data_for_range={
    "90-100":0,
    "100-110":0,
    "110-120":0,
    "120-130":0,
    "130-140":0
}
for height, occurrence in data.items():
    if 90<float(height)<100:
        mode_data_for_range["90-100"]+=occurrence
    elif 100<float(height)<110:
        mode_data_for_range["100-110"]+=occurrence
    elif 110<float(height)<120:
        mode_data_for_range["110-120"]+=occurrence
    elif 120<float(height)<130:
        mode_data_for_range["120-130"]+=occurrence
    elif 130<float(height)<140:
        mode_data_for_range["130-140"]+=occurrence

mode_range, mode_occurrence = 0,0
for range, occurrence in mode_data_for_range.items():
    if occurrence>mode_occurrence:
        mode_range, mode_occurrence = [int(range.split("-")[0]),int(range.split("-")[1])],occurrence
mode=float((mode_range[0]+mode_range[1])/2)
print(f"Mode is {mode:2f}")
