# 9- Image resizer

import sys
from PIL import Image

'''
# get path of img from user
while True:
    img_path = input("Enter path of img: ")
    try:
        # open img
        image = Image.open(img_path)
        break
    
    except IOError:
        print(f"There is Error : {IOError}")
'''


try:
    # open img
    image = Image.open('imgs_to_test/26.jpg')
except IOError:
    print(f"There is : {IOError}")
    sys.exit()

##### resize but with some problems of pixels 
# new_image = image.resize((2000, 2000))

##### resize img - with no problems
image.thumbnail((400, 400))

# save img im path
image.save('imgs_to_test/26___.jpg')
