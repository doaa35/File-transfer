import os
import shutil

# import imghdr
# 'imghdr' is deprecated and slated for removal in Python 3.13
# my python version dosen't support imghdr 
# so i created a list(img_lst) to check file type snd then get extension of file

def func(src, dest):

    img_lst=['jpg', 'jpeg', 'png']

    if not (os.path.exists(dest)):

        # Ensure destination directory exists; create it if necessary
        os.makedirs(dest, exist_ok=True)
    
    
    if os.path.exists(src):

        for root, dirs, files in os.walk(src):
            
            for file in files:
                file_path = os.path.join(root, file)

                tail = file.split('.')[1]
                
                if tail in img_lst:
                    # Move a file or directory from source to destination
                    shutil.move(file_path, dest)
            
        
        
    else:
        print("file dosen't exist")
    
           


# Example usage:

### get your dir full path
source_directory = r'src'

#dir exists 
### get your dir full path
# destination_directory = r'dst'

#dir not exists 
### get your dir full path
destination_directory = r'dest'

func(source_directory, destination_directory)
