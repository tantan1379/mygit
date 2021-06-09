'''
@File    :   split.py
@Time    :   2021/06/07 16:06:54
@Author  :   Tan Wenhao 
@Version :   1.0
@Contact :   tanritian1@163.com
@License :   (C)Copyright 2021-Now, MIPAV Lab (mipav.net), Soochow University. All rights reserved.

Notes: This script can only be used for the first time. If you want to resplit the dataset, it is a must to delete all the previous files first.
'''
# here put the import lib
import shutil
import os
import random

des_path = "F:\\Dataset\\CNV_Seg\\png_split_622\\"
des_img_path = des_path + "img"
des_mask_path = des_path + "mask"
origin_img_path = "F:\\Dataset\\CNV_Seg\\png\\all_imgs\\"
origin_label_path = "F:\\Dataset\\CNV_Seg\\png\\cnv_masks\\"

if not os.path.exists(des_img_path+os.sep+"train"):
    os.mkdir(des_img_path+os.sep+"train")
if not os.path.exists(des_img_path+os.sep+"val"):
    os.mkdir(des_img_path+os.sep+"val")
if not os.path.exists(des_img_path+os.sep+"test"):
    os.mkdir(des_img_path+os.sep+"test")
if not os.path.exists(des_mask_path+os.sep+"train"):
    os.mkdir(des_mask_path+os.sep+"train")
if not os.path.exists(des_mask_path+os.sep+"val"):
    os.mkdir(des_mask_path+os.sep+"val")
if not os.path.exists(des_mask_path+os.sep+"test"):
    os.mkdir(des_mask_path+os.sep+"test")

# image split
one_time_img_path_list = list()
one_time_label_path_list = list()
img_2_label = list()
for one_time_img in os.listdir(origin_img_path):
    one_time_img_path = os.path.join(origin_img_path,one_time_img)
    one_time_img_path_list.append(one_time_img_path)

for one_time_label in os.listdir(origin_label_path):
    one_time_label_path = os.path.join(origin_label_path,one_time_label)
    one_time_label_path_list.append(one_time_label_path)

for i in range(len(one_time_label_path_list)):
    img_2_label.append((one_time_img_path_list[i],one_time_label_path_list[i]))
# print(img_2_label)
random.shuffle(img_2_label)


for iter,(img,label) in enumerate(img_2_label):
    span = len(img_2_label)/10
    if iter<span*6:
        for one_img in os.listdir(img):
            shutil.copyfile(img+os.sep+one_img,os.path.join(des_img_path,"train",img.split(os.sep)[-1]+"_"+one_img))
        for one_label in os.listdir(label):
            shutil.copyfile(label+os.sep+one_label,os.path.join(des_mask_path,"train",img.split(os.sep)[-1]+"_"+one_label))
    elif 6*span<=iter<8*span:
        for one_img in os.listdir(img):
            shutil.copyfile(img+os.sep+one_img,os.path.join(des_img_path,"val",img.split(os.sep)[-1]+"_"+one_img))
        for one_label in os.listdir(label):
            shutil.copyfile(label+os.sep+one_label,os.path.join(des_mask_path,"val",img.split(os.sep)[-1]+"_"+one_label))
    else:
        for one_img in os.listdir(img):
            shutil.copyfile(img+os.sep+one_img,os.path.join(des_img_path,"test",img.split(os.sep)[-1]+"_"+one_img))
        for one_label in os.listdir(label):
            shutil.copyfile(label+os.sep+one_label,os.path.join(des_mask_path,"test",img.split(os.sep)[-1]+"_"+one_label))



