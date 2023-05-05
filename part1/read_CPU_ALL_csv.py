import glob
import csv

sumc = 0
CPUList={""}
MEMList={""}
file_path="C:/Users/manimalak/PycharmProjects/pythonProject/csv File/data.txt"

with open(file_path,"r")as file:
    contents = file.read()
    file.close()
    print(contents)
cpu_files=open("data.csv")
for line in cpu_files:
    if line.startswith("CPU_ALL"):
        line.lstrip(line,'CPU_ALL')

        sumc = sumc + 1
    elif line.startswith("MEM"):
        MEMlist
print(sumc)


#search for all files in the current directory that end in .txt
#cpu_files=glob.glob("data.txt/CPU_ALL*")
#print(cpu_files)