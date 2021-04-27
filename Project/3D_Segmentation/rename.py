import os
import glob
import re

root = 'F:\\Dataset\\gliomas\\3DT1'
all_images = []
for img in os.listdir(root):
    all_images+=glob.glob(os.path.join(root,img))

for img in all_images:
    n = img.split(os.sep)[-1]
    num = n.split("_")[1]
    print(num)
    os.rename(img,os.path.split())