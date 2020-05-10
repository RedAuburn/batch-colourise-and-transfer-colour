import urllib.request
import requests, json, sys, os
import blend_color_with_highres as bcwh

highrescolouroverlay = True
yourapikey = "enter api key here"


if(yourapikey and yourapikey!="enter api key here"):
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
else:
      print("you are using the default key, please consider signing up at deepai.org :)\n")
      os.system("start \"\" https://deepai.org/dashboard/profile")

input("press enter to exit")
