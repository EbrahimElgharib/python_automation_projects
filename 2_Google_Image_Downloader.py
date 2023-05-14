# 2_Google_Image_Downloader.py


import os
import requests
import urllib

# to download one img only
'''
img_url = 'https://blog.finxter.com/wp-content/uploads/2022/04/greenland_01a.jpg'
response_img = requests.get(img_url)

if response_img.status_code:
    # check if folder of imgs is Not Exist
    if not os.path.exists("folderName"):
        os.makedirs("folderName")
        
    fb = open("folderName/imgName.png", 'wb')
    fb.write(response_img.content)
    fb.close()
    print('success')

'''

# download list of imgs
imgs_urls = ['https://blog.finxter.com/wp-content/uploads/2022/04/greenland_01a.jpg',
        'https://blog.finxter.com/wp-content/uploads/2022/04/greenland_02a.jpg',
        'https://blog.finxter.com/wp-content/uploads/2022/04/greenland_03a.jpg',
        'https://blog.finxter.com/wp-content/uploads/2022/04/greenland_04a.jpg']
icount = 1


for i in imgs_urls:
    # check if folder of imgs is Not Exist
    if not os.path.exists("folderName"):
        os.makedirs("folderName")
    # do a task
    urllib.request.urlretrieve(i, f'FolderName/greenland_0{str(icount)}b.png')
    icount += 1

