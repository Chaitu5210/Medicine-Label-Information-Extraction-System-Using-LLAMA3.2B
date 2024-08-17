import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def medianFiltering():
    # getcwd() we return the current working directory
    current_directory = os.getcwd()
    # To get the path of the image 
    imagepath=os.path.join(current_directory,'Dataset\TestImg.jpg')
    image = cv.imread(imagepath)

    # initially opencv will take the image in BGR Format and then we will covnvert it into the RGB format which most of the libraries support
    imgRGB = cv.cvtColor(image,cv.COLOR_BGR2RGB)

    # imgFilter = cv.medianBlur(imgRGB,5) for using the median filtering
    
if __name__=='__main__':
    medianFiltering()