from tkinter import filedialog
import tkinter as tk
from PIL import Image
import sys, os

ftypes =[("image files","*.jpg;*.jpeg;*.png")]



#get images
def getimages(hrpathimport,cpathimport,imported):
    if(not imported):
        highrespath = tk.filedialog.askopenfilename(initialdir="/", title="Select highres image", filetypes=ftypes)
        colourpath = tk.filedialog.askopenfilename(initialdir=highrespath, title="Select colour image", filetypes=ftypes)
        return(highrespath,colourpath)
    if(imported):
        return(hrpathimport,cpathimport)

def scalecoloured(highrespath,colourpath):#done
    himgres = Image.open(highrespath).size
    cimg = Image.open(colourpath)
    cimg = cimg.resize(himgres,Image.BILINEAR)
    cimg.save(colourpath)

def colourblend(highrespath,colourpath):
    #for safety, convert highres to grayscale with this stuff
    #img = Image.open('image.png').convert('LA')
    #img.save('greyscale.png')
    return("nothing here yet\n")

    
#main 
def main(hrpathimport,cpathimport,importedtest):
    filepaths = getimages(hrpathimport,cpathimport,importedtest)
    if(filepaths[0] != "" or filepaths[1] != ""):
        scalecoloured(filepaths[0],filepaths[1])
        colourblend(filepaths[0],filepaths[1])
    else:
        print("please select two images\n")
    
    
if __name__ == "__main__":
    main("nothing entered yet\n","",False)
    


    
