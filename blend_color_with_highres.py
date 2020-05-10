from tkinter import filedialog
import tkinter as tk
import PIL
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

def scalecoloured(colourtoscale):
    #need to scale the coloured image to the same resolution as original highres to overlay.
    return("nothing here yet")

def colourblend(highresin,colourin):
    #for safety, convert highres to grayscale with this stuff
    #img = Image.open('image.png').convert('LA')
    #img.save('greyscale.png')
    return("nothing here yet")

    
#main 
def main(hrpathimport,cpathimport,importedtest):
    filepaths = getimages(hrpathimport,cpathimport,importedtest)
    scalecoloured(filepaths[1]) #will apply to image so don't need to assign
    colourblend(filepaths[0],filepaths[1]) 
    
    
if __name__ == "__main__":
    main("nothing entered yet","",False)
    


    
