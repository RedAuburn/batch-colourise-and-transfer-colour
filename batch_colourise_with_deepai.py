import urllib.request
import requests, json, sys, os
import blend_colour_with_highres as bcwh

highrescolouroverlay = True
seperatehiresfile = False #not working?
localscaleb4up = False #not used yet

yourapikey = ""

def main():
   if(yourapikey and yourapikey!="enter api key here"):
      newdir = os.path.join(os.getcwd(),r'colourised')
      print(newdir)
      if not os.path.exists(newdir):
         os.makedirs(newdir)
      for file in os.listdir("./input"):
          try:
                print("using: "+file)
                r = requests.post(
                   "https://api.deepai.org/api/colorizer",
                   files={'image': open(os.path.join("./input",file), 'rb'),},
                   headers={'api-key': yourapikey}
               )
                outlink = r.json()
                name= os.path.splitext(os.path.basename(file))
                newfilename = name[0]+"_colourised"+name[1]
                newfilepath = os.path.join(newdir,newfilename)
                originalfilepath = os.path.join("./input",file)
                urllib.request.urlretrieve(outlink["output_url"],newfilepath)
                print("created new file "+newfilename+"\n")
                if (highrescolouroverlay):
                   bcwh.main(originalfilepath,newfilepath,True,seperatehiresfile)
          except:
             print("skipping "+file+", not valid image.\n")
   else:
         print("you are using the default key, please consider signing up at deepai.org :)\n")
         os.system("start \"\" https://deepai.org/dashboard/profile")

   input("press enter to exit")
   
if __name__ == "__main__":
    main()
    


