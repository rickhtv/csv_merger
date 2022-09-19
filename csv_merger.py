# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 10:28:13 2022

@author: Rodolfo Henrique T. Valentin

CSV Merger, Combines all of the csv files inside the directory informed into a sigle csv file
"""
#Imports 
import os
import glob
import pandas as pd

#Search all csv files inside the folder specified in the os.chdir 
os.chdir("Base/")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')
