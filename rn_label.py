import os
file = os.listdir('label')

os.chdir('label')
for i in file:
    data = i.split('.')
    data1 = data[0] + ".txt"
    os.rename(i, data1)

# aps 2
import os
path = "label"

filelist = os.listdir(path)
os.chdir(path)

for i in filelist:
    data = i.split('.')
    process = data[0] + "_." + data[1]
    os.rename(i, process)
    print(f"processing : {process}")