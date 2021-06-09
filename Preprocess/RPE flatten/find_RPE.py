import shutil
import SimpleITK as sitk
import cv2
from PIL import Image
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

def get_max_index(matrix): 
    max_index_list = list()
    for j in range(len(matrix[0])):
        one_list=[]
        for i in range(len(matrix)):
            one_list.append(int(matrix[i][j]))
        max_index_list.append(one_list.index(max(one_list)))
    return max_index_list

def get_PRE_index(matrix):
    i = 0
    RPE_index_list = list()
    for j in range(len(matrix[0])):
        trigger = True
        for i in range(len(matrix)-1,-1,-1):
            if int(matrix[i-8][j])-int(matrix[i][j])>=70:
                RPE_index_list.append(i-8)
                # print(matrix[i-8][j],matrix[i][j])
                trigger = False
                temp = i-8
                break
        if trigger:
            RPE_index_list.append(temp)
        increase_time = 0
        decrease_time = 0
        if(j>1):
            if RPE_index_list[j]-RPE_index_list[j-1]>1 and increase_time<5:
                increase_time+=1
                last_index = RPE_index_list[j-1]
                RPE_index_list.pop()
                RPE_index_list.append(last_index+1)
            elif RPE_index_list[j]-RPE_index_list[j-1]<-1 and decrease_time<5:
                decrease_time+=1
                last_index = RPE_index_list[j-1]
                RPE_index_list.pop()
                RPE_index_list.append(last_index-1)
            else:
                increase_time = 0
                dncrease_time = 0
    return RPE_index_list

def get_RPE_curve_index(matrix):
    yvals_int = []
    RPE_index_list = get_PRE_index(matrix)
    x = [x for x in range(len(matrix[0]))]
    f1 = np.polyfit(x,RPE_index_list, 5)
    p1 = np.poly1d(f1)
    yvals = p1(x)
    for y in yvals:
        yvals_int.append(int(y))
    return yvals_int

if __name__ == '__main__':
    # 读入图片
    img_array = sitk.GetArrayFromImage(sitk.ReadImage("./testset/00000758.nii.gz"))
    one_img_array = img_array[1]
    # -------------------------------
    # 矩阵转图片
    # -------------------------------
    cv2.imwrite("1.jpg", one_img_array)
    img = cv2.imread("1.jpg")
    yvals = get_RPE_curve_index(one_img_array)
    yvals.pop()
    plt.imshow(one_img_array)
    # plot1 = plt.plot([x for x in range(512)],res, 'g',label='original values')
    plot2 = plt.plot([x for x in range(511)], yvals, 'r',label='polyfit values')
    plt.show()