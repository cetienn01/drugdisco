import sys, os, shutil
# ------------------------------- #
# This script collects all the molecules that passed a defined energy filter in docking and are collected in a list
# like the following (generated by the script 2_RetrieveLowestEnergy.sh)
#
# /netscr/mconvert/sod1/243/001/ZINC28294531.min.mol2   01.7646.pdb   4   -49.2703
# /netscr/mconvert/sod1/243/002/ZINC28380362.min.mol2   10.23874.pdb   1   -47.7001
# /netscr/mconvert/sod1/086/002/ZINC03173047.min.mol2   07.21963.pdb   1   -46.7343
# /netscr/mconvert/sod1/208/009/ZINC19707853.min.mol2   10.8479.pdb   1   -46.7139
#
# To run this script you need a list like the above.
#
# Attention: change the variables where indicated in the script and create the 'collectdir' folder
#
# Command:
# 4_RetrieveMolShortList.sh mconvert_list
# ------------------------------- #
# - variables to change - #
collectdir="retrieved_10_docking"
wrkdir="./netscr/mconvert/sod1"
# - - - - - - - - - - - - #

listfile=sys.argv[1]

if os.path.exists(str(listfile)):
    #print listfile
    with open(str(listfile), "r") as f:
        lines = f.readlines()
        for line in lines:
            filename = line.rstrip().split()[0]
            print filename
            dst = wrkdir + "/" + collectdir + "/" + os.path.basename(filename)
            #print dst
            shutil.copyfile(filename, dst)
            

