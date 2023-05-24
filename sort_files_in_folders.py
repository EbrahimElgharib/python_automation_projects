# Ebrahi Elsayed Elgharib 
# 24-5-2023 at 12:33:00 AM

import os
import shutil

# lists of my possible extensions
audio_ext = ['aif', 'cda', 'mid', 'mp3', 'mpa', 'ogg', 'wav', 'wma', 'wpl','ac3','m4a']
compressed_ext = ['7z', 'arj', 'deb', 'pkg', 'rar', 'rpm', 'targz', 'z', 'zip']
disk_media_ext = ['bin', 'dmg', 'iso', 'toast', 'vcd']
data_ext = ['csv', 'dat', 'db', 'log', 'mdb', 'sav', 'sql', 'tar', 'xml']
email_ext = ['email', 'eml', 'emlx', 'msg', 'oft', 'ost', 'pst', 'vcf']
exe_ext = ['apk', 'bat', 'bin', 'cgi', 'com', 'exe', 'gadget', 'jar', 'msi', 'wsf']
font_ext = ['fnt', 'fon', 'otf', 'ttf']
image_ext = ['ai', 'bmp', 'gif', 'ico', 'jpeg', 'png','jpg', 'ps', 'psd', 'svg', 'tif', 'webp']
programming_ext = ['c','pl', 'cgi', 'class', 'cpp', 'cs', 'h', 'java', 'php', 'py', 'sh', 'swift', 'vb','html','xhtml','css']
video_ext = ['3g2', '3gp', 'avi', 'flv', 'h264', 'm4v', 'mkv', 'mov', 'mp4', 'mpg', 'rm', 'swf', 'vob', 'webm', 'wmv']
documents_ext = ['doc','docx', 'odt', 'pdf', 'rtf', 'tex', 'txt', 'wpd', 'ods', 'xls', 'xlsm', 'xlsx', 'key', 'odp', 'pps', 'ppt', 'pptx']


# make them in a dict
all_ext = {
    'audio_ext' : audio_ext,
    'compressed_ext' : compressed_ext,
    'disk_media_ext' : disk_media_ext,
    'data_ext' : data_ext,
    'email_ext' : email_ext,
    'exe_ext' : exe_ext,
    'font_ext' : font_ext,
    'image_ext' : image_ext,
    'programming_ext' : programming_ext,
    'video_ext' : video_ext,
    'documents_ext' : documents_ext
}

# this function to move file to it's correct folder
def my_move(file_info, folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    shutil.move(file_info, folder_name)

# open path folder that contain all sources
directory_path = 'data' # data folder path
os.chdir(directory_path) # go to this path

files_info = os.listdir() # get info of files in this folder.

# loop around all files
for file_info in files_info:
    # check if this file is a directory ---> do nothing
    if os.path.isdir(file_info):
        continue
    # get extension of file
    # if no "." in file name ---> make ext is empty
    if '.' in file_info:
        ext = file_info.split('.')[-1] 
    else:
    # so there is (no) extension ---> move to no_ext folder
        my_move(file_info, 'no_ext')
        continue

    # search if extension of file is exist or not
    done = False
    for ext_list in all_ext.items():
        # search if exist
        if ext in ext_list[1]:
            my_move(file_info, ext_list[0])
            done = True
            break
    # check if ext is not found ---> move to Not_Found Folder
    if not done:
        my_move(file_info, 'Not_Found')
    



           

        

    