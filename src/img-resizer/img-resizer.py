import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

inputFolder  = os.path.join(os.getcwd(), 'dataset', 'dataset-original')
outputFolder = os.path.join(os.getcwd(), 'dataset', 'dataset-resized')
resolution   = tuple((640,640))

if os.path.exists(outputFolder) is False:
    os.mkdir(outputFolder)

for filename in os.listdir(inputFolder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        img_org = cv2.imread(inputFolder + '/' + filename)
        img_res = cv2.resize(img_org, resolution)
        cv2.imwrite(os.path.join(outputFolder, filename), img_res)
    else:
        continue

#debug string
print(cv2.__version__)