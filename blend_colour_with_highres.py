from tkinter import filedialog
import tkinter as tk
from PIL import Image
import sys, os

ftypes =[("image files","*.jpg;*.jpeg;*.png")]

#go away tk window
root = tk.Tk()
root.withdraw()

#get image paths when standalone or when using parameters from another script
def getimages(hrpathimport,cpathimport,imported):
    if(not imported):
        highrespath = tk.filedialog.askopenfilename(initialdir="/", title="Select highres image", filetypes=ftypes)
        colourpath = tk.filedialog.askopenfilename(initialdir=highrespath, title="Select colour image", filetypes=ftypes)
        return(highrespath,colourpath)
    if(imported):
        return(hrpathimport,cpathimport)
    
#scales the coloured image to the same size as the high res.
def scalecoloured(highrespath,colourpath,seperatefile):
    himgres = Image.open(highrespath).size
    cimg = Image.open(colourpath)
    cimg = cimg.resize(himgres,Image.BILINEAR)
    saveimg(cimg,colourpath,seperatefile) #doesnt work when seperate file enabled 
    
#splits the HS channels from colour image, merges it with V from the high res. (ps color blend mode)
def colourblend(highrespath,colourpath,seperatefile):
    colourhs = Image.open(colourpath).convert("HSV")
    colourh = colourhs.getchannel(0)
    colours = colourhs.getchannel(1)
    hiresv = Image.open(highrespath).convert("L") 
    final = Image.merge("HSV",(colourh,colours,hiresv))
    final = final.convert("RGB")
    saveimg(final,colourpath,seperatefile)
    
def saveimg(image,path,seperatefile):
    if(seperatefile):
        newpath = os.path.dirname(path)
        newname= os.path.splitext(os.path.basename(path))
        newpath = newpath+"/highrescolourised/"+newname[0]+"_hires_colourised"+newname[1]
        try:
            os.mkdir(os.path.dirname(newpath))
        except:
            print("")
        image.save(newpath)
    else:
        image.save(path)
    
    
#main 
def main(hrpathimport,cpathimport,importedtest,seperatefile):
    filepaths = getimages(hrpathimport,cpathimport,importedtest)
    if(filepaths[0] and filepaths[1]):
        print("starting colour image scaling...")
        scalecoloured(filepaths[0],filepaths[1],seperatefile)
        print("finished colour image scaling\n")
        print("starting image blending...")
        colourblend(filepaths[0],filepaths[1],seperatefile)
        print("finished image blending\n")
    else:
        print("please select two images\n")
    
#to prevent script being run on import in other scripts.  
if __name__ == "__main__":
    runfrommain = True
    main("nothing entered yet\n","",False,False)
