import csv
import fileinput 
import os
import pyaudio
import wave
import subprocess, sys

#path = r'D:\openfinalsmile\soundcsv'#27
path = r'D:\openfinalsmile\soundsample\test\csv'#39
data = {}
for dir_entry in os.listdir(path):
    dir_entry_path = os.path.join(path, dir_entry)
    if os.path.isfile(dir_entry_path):
      
       #newf=dir_entry_path[0:27]+'0Cut\z'+dir_entry_path[27:-4]+'.csv'
       newf=dir_entry_path[0:39]+'0Cut\z'+dir_entry_path[39:-4]+'.csv'
       print newf
       #oldf=dir_entry_path[0:27]+dir_entry_path[27:-4]+'.csv'
       oldf=dir_entry_path[0:39]+dir_entry_path[39:-4]+'.csv'
       print oldf
       writer = csv.writer(open(newf, "w"))
       count =0;
       silencevalue = ''
       for row in csv.reader(open(oldf)):
       	 if count == 0:
       		writer.writerow(row)
       	 if count == 1:
        		silencevalue = row[0].split(';')[2]
        		print silencevalue
       
         count = count+1
       	 if not row[0].endswith(silencevalue):
       		writer.writerow(row)
       #writer.closed
print "\n\n-----------------------------------------------------------------------\n"
print "----------------------- Emotion Training System  ----------------------\n"
print "-----------------------------------------------------------------------\n"
    
print("\nRemoved noise values !\n")
s=raw_input("press enter to continue")
print("s")
subprocess.Popen("recordEnergySelect.py", shell=True)