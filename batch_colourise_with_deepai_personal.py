import urllib.request
import requests
import json
import sys
import os
import blend_color_with_highres as bcwh

highrescolouroverlay = True
yourapikey = "a884a504-5db5-45b7-9299-906cb5ed93ae"



if(yourapikey == "a884a504-5db5-45b7-9299-906cb5ed93ae"):
   print("you are using the default key, please consider signing up at deepai.org :)")

newdir = os.path.join(os.getcwd(),r'colourised')
if not os.path.exists(newdir):
   os.makedirs(newdir)

for file in os.listdir():
    try:
          print("using: "+file)
          r = requests.post(
             "https://api.deepai.org/api/colorizer",
             files={'image': open(file, 'rb'),},
             headers={'api-key': yourapikey}
         )
          outlink = r.json()
          newfilename = os.path.splitext(os.path.basename(file))[0]+"_colourised.jpg"
          newfilepath = os.path.join(newdir,newfilename)
          originalfilepath = os.path.abspath(file)
          urllib.request.urlretrieve(outlink["output_url"],newfilepath)
          print("created new file "+newfilename+"\n")
          if (highrescolouroverlay):
             bcwh.main(originalfilepath,newfilepath,True)
    except:
        print("skipping "+file+", not valid image.\n")

input("press enter to exit")
