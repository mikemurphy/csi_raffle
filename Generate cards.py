# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 15:02:19 2018

@author: MMURPHY
"""

# Read in csv file
# Iterate through csv file mytex.writing parameters

#Libraries
import pandas as pd

# Import csv
path = "my_path"
my_csv = pd.read_csv(path+"scratch_cards_example.csv")
my_csv['pic1'] = my_csv['pic1'].astype(str)
my_csv['pic2'] = my_csv['pic2'].astype(str)
my_csv['pic3'] = my_csv['pic3'].astype(str)
my_csv['pic4'] = my_csv['pic4'].astype(str)    
my_csv['specialpic'] = my_csv['specialpic'].astype(str)       
my_csv['cardnr'] = my_csv['cardnr'].astype(str)            


# Function for top of page
def latex_header():    
	mytex.write('\\documentclass{beamer}')
	mytex.write('\\usepackage[absolute,overlay]{textpos}')
	mytex.write('\\usepackage{graphicx}')
	mytex.write('\\usepackage[utf8]{inputenc}')
	mytex.write('\\usepackage[export]{adjustbox}')
	mytex.write('\\begin{document}')
	mytex.write('\n')    
    
# Function for text block
def add_text(x,y):
    mytex.write('\\begin{textblock*}{5cm}('+x+'cm,'+y+'cm)')
    mytex.write('\\texttt{\detokenize{Rs.__________}}')
    mytex.write("\\end{textblock*}"+'\n')    

# Function for hidden amount    
def add_amount(x,y,amount):
    mytex.write('\\begin{textblock*}{5cm}('+x+'cm,'+y+'cm)')
    mytex.write("\\fbox{Rs. "+amount+"}")
    mytex.write("\\end{textblock*}"+'\n')
           
# Function for text with entry 
def add_field(x,y,var,value):    
    mytex.write('\\begin{textblock*}{5cm}('+x+'cm,'+y+'cm)')
    mytex.write(var+": " + value)
    mytex.write('\\end{textblock*}'+'\n')    
    
# Function for piture   
def add_picture(x,y,filepath):

    mytex.write('\\begin{textblock*}{5cm}('+x+'cm,'+y+'cm)')
    string = "\includegraphics[width=2.5cm, height=1.5cm]{"
    mytex.write(string+filepath+"}")
    mytex.write('\\end{textblock*}'+'\n')

# Generate cards
mytex = open('scratch_cards.tex','w')

latex_header()
for index, row in my_csv.iterrows():      
    mytex.write('\\begin{frame}')

    # Pictures 
    add_picture("1","1",str(row['pic1'])+".png")
    add_picture("4","1",str(row['pic2'])+".png")
    add_picture("7","1",str(row['pic3'])+".png")
    add_picture("10","1",str(row['pic4'])+".png")
    add_picture("1","6",str(row['specialpic'])+".png")
    
    # Amounts
    add_text("1.1","3") # Amount 1
    add_text("4.1","3") # Amount 2
    add_text("7.1","3") # Amount 3    
    add_text("10.1","3") # Amount 4
    add_amount("4","6.25",str(row['premwin'])) # Special amount

    # Text fields
    add_field("7","4","Card ",str(row['cardnr']))
    add_field("7","4.5","Farmer Name"," ")    
    add_field("7","5","Farmer ID"," ")
    add_field("7","5.5","Village"," ")

    # Field for recording amount
    mytex.write('\\begin{textblock*}{5cm}(7cm,7.5cm)')
    mytex.write('\\texttt{\detokenize{Rs.__________}}')
    mytex.write('\\end{textblock*}'+'\n')

    # Special offer labels
    mytex.write('\\begin{textblock*}{5cm}(1.75cm,5cm)')
    mytex.write('\\textbf{Special premium offer}')
    mytex.write('\\end{textblock*}'+'\n')
    
    mytex.write('\\begin{textblock*}{5cm}(1.2cm,5.7cm)')
    mytex.write('\\tiny{Product offered:}')
    mytex.write('\\end{textblock*}'+'\n')
    
    mytex.write('\\begin{textblock*}{5cm}(4.2cm,5.7cm)')
    mytex.write('\\tiny{Premium to pay:}')
    mytex.write('\\end{textblock*}'+'\n')
    
    # Other labels
    mytex.write('\\begin{textblock*}{5cm}(7cm,6.5cm)')
    mytex.write('Amount to be paid by farmer')
    mytex.write('\\end{textblock*}')
    
    mytex.write('\\begin{textblock*}{10cm}(2cm,8.25cm)')
    mytex.write('\\tiny{\it {WRITE 0 IF NOT WILLING TO PAY SPECIAL PREMIUM OFFER FOR SELECTED PRODUCT.}}')
    mytex.write('\\end{textblock*}'+'\n')

    mytex.write('\\end{frame}'+'\n')

# End of frame
mytex.write('\\end{document}')         
mytex.close()