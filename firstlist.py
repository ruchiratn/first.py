fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened',fname)
    quit()
lst = list()
for line in fh:
    para = line.rstrip()
    fls = para.split()
    i=0
    for i in fls:
        if i in lst: continue
        lst.append(i)
lst.sort()
print(lst)
