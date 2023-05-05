import glob
import csv


CPUList = list()
MEMList = list()
#file_path="C:/Users/manimalak/PycharmProjects/pythonProject/csv File/data.txt"
file_path = "C:/Users/akshaypa/PycharmProjects/python/data.txt"

with open(file_path,"r")as file:
    contents = file.read()
    file.close()
    print(contents)
cpu_files=open("data.csv")
for line in cpu_files:
    if line.startswith("CPU_ALL"):
        CPUList.append(line.replace("CPU_ALL,", ''))
    elif line.startswith("MEM"):
        MEMList.append(line.replace("MEM,", ''))
print("Data from CPU is as follows: ", CPUList)
print("Data from MEM is as follows: ", MEMList)


