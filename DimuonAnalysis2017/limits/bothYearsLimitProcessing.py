import os
import subprocess
import commands
import re
from glob import glob
import sys
from shutil import move
test = False

year = "2017"

if not os.path.isdir("combine_output/bothYears"):
        os.makedirs("combine_output/bothYears")

files = glob("output/dpCard_"+year+"IterV3_*.txt")
for fname in files:
	m = re.search(r"_m(\d+\.?\d+)_", fname).group(1)
	d = re.search(r"_(\d+).txt", fname).group(1)
	print "ID {0},  m={1}".format(d,m)

        paramLimits = ""

#        errs = open('errorParams2017.txt', 'r').read()
#        for line in errs.split("\n"):
#                if "massPoint"+m in line:
#                        paramLimits = line[15:]

	if test and (not int(d)%10==0): continue
	if (os.path.isfile(fname)):
                os.system("combineCards.py output/dpCard_2017IterV3_m"+m+"_"+d+".txt output/dpCard_2018IterV3_m"+m+"_"+d+".txt > output/dpCard_IterV3_m"+m+"_"+d+".txt")
                #os.system("combine -M AsymptoticLimits output/dpCard_IterV3_m"+m+"_"+d+".txt -m "+m+" -n asympMassIndex_"+d+ " --cminDefaultMinimizerStrategy 0 --setParameters pdf_index=0 -v 2")	
                #os.system("combine -M AsymptoticLimits output/dpCard_IterV3_m"+m+"_"+d+".txt -m "+m+" -n asympMassIndex_"+d)	
                #if ((float(m) == 1.716) or (float(m) == 2.157)):
                 #       os.system("combine -M AsymptoticLimits output/dpCard_IterV3_m"+m+"_"+d+".txt -m "+m+" -n asympMassIndex_"+d+" --setParameters pdf_index_2017=0,pdf_index_2018=0 --rAbsAcc=0.0001 --rRelAcc=0.0001 --freezeParameters pdf_index_2017,pdf_index_2018 --cminDefaultMinimizerStrategy 0")
                #print("combine -M AsymptoticLimits output/dpCard_IterV3_m"+m+"_"+d+".txt -m "+m+" -n asympMassIndex_"+d+" --setParameters pdf_index_2017=0,pdf_index_2018=0")
                #else:
                os.system("combine -M Significance --pvalue output/dpCard_IterV3_m"+m+"_"+d+".txt -m "+m+" -n asympMassIndex_"+d+ " --cminDefaultMinimizerStrategy 0  --setParameters pdf_index_2017=0,pdf_index_2018=0  --rMin -1 --rMax 1") 
                #os.system("combine -M AsymptoticLimits output/dpCard_IterV3_m"+m+"_"+d+".txt -m "+m+" -n asympMassIndex_"+d+" --setParameters pdf_index_2017=0,pdf_index_2018=0 --rAbsAcc=0.0001 --rRelAcc=0.0001 --cminDefaultMinimizerStrategy 0 --rMin -1 --rMax 1")	
                #                print("combine -M AsymptoticLimits output/dpCard_IterV3_m"+m+"_"+d+".txt -m "+m+" -n asympMassIndex_"+d+" "+paramLimits)
outfiles = glob("higgsCombineasympMassIndex_*.root")
for of in outfiles:	
	move(of, "combine_output/bothYears/")
