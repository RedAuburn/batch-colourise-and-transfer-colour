# batch-colourise-and-transfer-colour
 A Python script to batch colourise photos and transfer colour to the high res original. colourising is currently done with the deepAI API, which uses Jason Antic's model.  https://deepai.org/machine-learning-model/colorizer
 
 This could also be applicable for downsizing videos and overlaying colour to the highres original, drastically reducing the time needed to colourise a video.
 
 examples:
![Gif Demo](https://github.com/endim8/batch-colourise-deepai/blob/master/Example/gifdemo.gif)
![Close Cubes](https://github.com/endim8/batch-colourise-deepai/blob/master/Example/sidebyside.png)
 
 ## Run:
 - Place your images into the `input` folder
 
 - Open a terminal/cmd and `cd` into the folder 
 
 - Run `python3 batch_colourise_with_deepai.py`
 
 ## Features:
 - batch process a folder of images with the DeepAI API
 
 - Overlay colour from the low res colourised image onto the original full res image automatically. (similar to PS Color blendmode)
 
 - Overlay can be used for individual image sets.
 
 ## Todo:
- [ ] scale image to upload locally
 
- [ ] proper GUI
 
- [ ] select folder instead of putting script in it
 
- [ ] select only individual files mode (done for blend but not batch, just run blend on it's own)
 
- [x] local file input sanitization when selecting files
