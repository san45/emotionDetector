
from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave
import os
import csv
import subprocess, sys
import csv
import os
energy=[];
#path = r'D:\openfinalsmile\soundcsv'#27


path = r'D:\openfinalsmile\soundsample\test\csv\0Cut'#39
data = {}
for dir_entry in os.listdir(path):
    dir_entry_path = os.path.join(path, dir_entry)
    if os.path.isfile(dir_entry_path):

#os.system('SMILExtract -C config/demo/demo1_energy.conf -I hithashappy.wav -O hithashappy.csv')
#os.system('SMILExtract -C config/prosodyShs.conf -I hithahappy.wav -O hithahappy.csv')
		if dir_entry_path[-10:]=="Energy.csv":
		      i=0;
		      sum=0;
		      with open(dir_entry_path) as f:
		        reader = csv.DictReader(f, delimiter=';')
		        rows = list(reader)



		      def num (s):
		            return float(s)


		      for row in rows:
		        sum+=abs(num(row['pcm_LOGenergy']))
		        i=i+1;
		         #sum+=num(row['pcm_loudness_sma'])
		         #print row['pcm_LOGenergy']
		      print "sum is",sum
		      print i

		      print dir_entry_path,"===>>",sum/i
		      energy.append(sum/i)

		else:
		      i=0;
		      sum=0;
		      with open(dir_entry_path) as f:
		        reader = csv.DictReader(f, delimiter=';')
		        rows = list(reader)



		      def num (s):
		            return float(s)


		      for row in rows:
		        sum+=abs(num(row['pcm_loudness_sma']))
		        i=i+1;
		         #sum+=num(row['pcm_loudness_sma'])
		         #print row['pcm_LOGenergy']
		      print "sum is",sum
		      print i

		      print dir_entry_path,"===>>",sum/i
		      energy.append(sum/i)

print "\n\n-----------------------------------------------------------------------\n"
print "----------------------- Emotion Training System  ----------------------\n"
print "-----------------------------------------------------------------------\n"
    
print("Selected values are :")
print "\nenergy",energy[0]
print "\nloudness",energy[1]

print "-----------------------------------------------------------------------\n"
happ=20.22;
if energy[1]<.4 :
	print "Please speak bit more clearly"
elif energy[1]<.5 :
	happ=happ+70.2
elif energy[1]<.55:
	happ=happ+60.9
elif energy[1]<.56 :
	happ=happ+50.78
elif energy[1]<.6 :
	happ=happ+40.4
else :
	happ=happ+20

sad=40.22
if energy[1]<.4 :
	print "Please speak bit more clearly"
elif energy[1]>.7 :
	sad=sad+70.2
elif energy[1]>.65:
	sad=sad+60.9
elif energy[1]>.63 :
	sad=sad+50.78
elif energy[1]>.6 :
	sad=sad+40.4
else :
	sad=sad+20


print "happy ",happ
print "\nsad",sad

if happ > sad :
	sad=abs(100-happ)
else :
	happ=abs(100-sad)
print ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n"
print  "happiness",happ,"%"
print "sadness",sad,"%"




s=raw_input("\npress enter to continue")