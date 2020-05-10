# batch-colourise-deepai
 A Python script to batch colourise photos and transfer colour to the high res original. colourising is done with the deepAI API, which uses Jason Antic's model.  https://deepai.org/machine-learning-model/colorizer
 
 This could also be applicable for downsizing videos and overlaying colour, drastically reducing the time needed to colourise a video.
 
 examples:
![Gif Demo](https://github.com/endim8/batch-colourise-deepai/blob/master/Example/gifdemo.gif)
![Close Cubes](https://github.com/endim8/batch-colourise-deepai/blob/master/Example/sidebyside.png)
 ## Setup:
 To setup, install the dependencies by running install-dependencies.bat (you need pip)
 
 ## Run:
 to run, place your images into the script folder and run batch_colourise_with_deepai.py.
 
 ## Features:
 - batch process a folder of images with the DeepAI API
 
 - Overlay colour from the low res colourised image onto the original full res image automatically. (similar to PS Color blendmode)
 
 - Overlay can be used for individual image sets.
 
 ## Todo:
 - proper GUI
 
 - select folder instead of putting script in it
 
 - select only individual files mode (done for blend but not batch, just run blend on it's own)
 
 - local file input sanitization when selecting files
 
 - run DeOldify locally instead of using API for better quality
