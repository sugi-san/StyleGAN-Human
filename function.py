# --- display_mp4 ---
from IPython.display import display, HTML
from IPython.display import HTML

def display_mp4(path):
    from base64 import b64encode
    mp4 = open(path,'rb').read()
    data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
    display(HTML("""
    <video width=700 controls>
        <source src="%s" type="video/mp4">
    </video>
    """ % data_url))
    #print('Display finished.')  ###


# --- display_pic ---
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
import glob

def display_pic(folder):
    fig = plt.figure(figsize=(15, 60))
    files = sorted(glob.glob(folder+'/*.png'))
    files.sort()
    for i, file in enumerate(files):
        img = Image.open(file)    
        images = np.asarray(img)
        ax = fig.add_subplot(10, 5, i+1, xticks=[], yticks=[])
        image_plt = np.array(images)
        ax.imshow(image_plt)
        name = os.path.basename(file)
        ax.set_xlabel(name, fontsize=20) 
    fig.tight_layout()
    plt.show()
    plt.close()


# --- reset_folder ---
import shutil

def reset_folder(path):
    if os.path.isdir(path):
      shutil.rmtree(path)
    os.makedirs(path,exist_ok=True)
    
