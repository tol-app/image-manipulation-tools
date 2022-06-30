import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

inputFolder  = 'dataset/dataset-original'
outputFolder = 'dataset/dataset-resized'
resolution   = tuple((640,640))

if os.path.exists(outputFolder) is True:
    try:
        os.mkdir(outputFolder)
    except AssertionError:
            print ("Output path does not exist")

for filename in os.listdir(inputFolder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        img_org = cv2.imread(filename)
        img_res = cv2.resize(img_org, resolution)
        cv2.imwrite(os.path.join(outputFolder, filename), img_res)
    else:
        continue

print(cv2.__version__)