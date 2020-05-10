from tkinter import filedialog
import tkinter as tk
import PIL as pl
import sys
import os

ftypes =[("image files","*.jpg;*.jpeg;*.png")]



#get images

def getimages(hrpathimport,cpathimport,imported):
    if(not imported):
        highrespath = tk.filedialog.askopenfilename(initialdir="/", title="Select highres image", filetypes=ftypes)
        colourpath = tk.filedialog.askopenfilename(initialdir=highrespath, title="Select colour image", filetypes=ftypes)
        return(highrespath,colourpath)
    if(imported):
        return(hrpathimport,cpathimport)

    
#main 
def main(hrpathimport,cpathimport,importedtest):
    return getimages(hrpathimport,cpathimport,importedtest)
    
if __name__ == "__main__":
    print(main("","",False))


    
#colourimg = pl.Image.open(filepath)

