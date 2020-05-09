import requests
import os
import json
import urllib.request

yourapikey = "a884a504-5db5-45b7-9299-906cb5ed93ae" #this is the default key

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
        urllib.request.urlretrieve(outlink["output_url"],os.path.join(newdir,newfilename))
        print("created new file "+newfilename+"\n")
    except:
        print("skipping "+file+", not valid image.\n")

input("press enter to exit")
