Black and White MapRoad Segments MapFinal Sketch Map
1. PyRoadmap
PyRoadmap is a python script that generates a road map based on a 2d image. It takes satellite map images as input and generates a sketch map after calculations. We can split the script into three parts :

1.   Image Manipulation - This involves loading the image then adjusting the image for better calculation.
2.  Pixel Crawling - This involves crawling through the image matrix to identify road segments.
3.  Rendering - The final part involves rendering a 2D roadmap image based on the segment identification.
Libraries Used: cv2, pyGame, numPy
How it works.
Firstly, it loads images using OpenCV (cv2). The loaded image is then down-sized for faster calculations. Once the image has been down-sized, the script makes some brightness and contrast adjustments on the image, separating the environment from the road. Then the RGB image is converted to a B&W image. As a result, the image NumPy array has 1s and 0s values instead of RGB values to denote dark and bright pixels. The second image shows the output of the above steps. Then a crawler function is deployed to detect a continuous path of dark pixels referred to as segments. The crawler function stores the pixel's index in an array to avoid rechecking the pixels. Rechecking pixels can create reassociating of pixels. It also slows down the overall performance. Briefly, Pixels are only checked once for a continuous path. The third image shows the formation of segments. After the identification of all the road segments, pyRoadmap generates a 2D roadmap. For this, the script draws a line connecting the starting and ending point of the road segment. Finally, the script generates the final roadmap after looping through the segment array.

Findings
1.  The better way for segment identification would be to use a matrix to detect turns. The continuous path method works well only if the road is less complex and does not have too many connected turns. Also, because roads cannot be fully isolated from the environment using only image manipulation, the crawler confuses some environmental aspects such as houses, trees as part of the segment. As a result, scratchy patterns can be seen all over the rendered roadmap.
2.  If the identification of segments has higher accuracy, linear regression would be a better approach to generate the final roadmap.
3.  Just use ML. Life is easier that way.
