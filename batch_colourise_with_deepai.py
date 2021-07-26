import urllib.request
import requests, json, sys, os, webbrowser
import blend_colour_with_highres as bcwh

highrescolouroverlay = True
seperatehiresfile = False #not working?
localscaleb4up = False #not used yet
yourapikey = ""

with open(os.path.realpath("APIKey.txt")) as f:
    yourapikey = f.read().split()[0]
    print("\n	api key used: "+yourapikey+"\n")

def main():
      newdir = os.path.join(os.getcwd(),r'colourised')
      if not os.path.exists(newdir):
         os.makedirs(newdir)
      for file in os.listdir("./input"):
          try:
              file_extension = str.lower(os.path.splitext(file)[1])
              if(file_extension in [".jpeg", ".jpg", ".png", ".bmp"]):
                    print("using: " + file)
                    r = requests.post(
                       "https://api.deepai.org/api/colorizer",
                       files={'image': open(os.path.join("./input",file), 'rb'),},
                       headers={'api-key':yourapikey}
                    )
                    print(r.json())
                    outlink = r.json()
                    name= os.path.splitext(os.path.basename(file))
                    newfilename = name[0]+"_colourised"+name[1]
                    newfilepath = os.path.join(newdir,newfilename)
                    originalfilepath = os.path.join("./input",file)
                    urllib.request.urlretrieve(outlink["output_url"],newfilepath)
                    print("created new file "+newfilename+"\n")
                    if (highrescolouroverlay):
                       bcwh.main(originalfilepath,newfilepath,True,seperatehiresfile)
                    webbrowser.open(os.path.realpath(os.path.split(newfilepath)[0]))
              else:
                  print("skipping " + file + ", not a valid image.\n")
          except:
          	print("you need an API key, please consider sign up for one at deepai.org :)\n")
          	webbrowser.open("https://deepai.org/dashboard/profile")

if __name__ == "__main__":
    main()
    input("press enter to exit")
