import shutil
import SimpleITK as sitk
import cv2
from PIL import Image
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# 自动分割（无法有效分割有病灶的情况）
def get_PRE_index(matrix):
    i = 0
    RPE_index_list = list()
    for j in range(len(matrix[0])):
        trigger = True
        for i in range(len(matrix)-1, -1, -1):
            if int(matrix[i-8][j])-int(matrix[i][j]) >= 85:
                RPE_index_list.append(i-8)
                # print(matrix[i-8][j],matrix[i][j])
                trigger = False
                temp = i-8
                break
        if trigger:
            RPE_index_list.append(temp)
        if(j > 1):
            if RPE_index_list[j]-RPE_index_list[j-1] > 1:
                last_index = RPE_index_list[j-1]
                RPE_index_list.pop()
                RPE_index_list.append(last_index+1)
            elif RPE_index_list[j]-RPE_index_list[j-1] < 1:
                last_index = RPE_index_list[j-1]
                RPE_index_list.pop()
                RPE_index_list.append(last_index-1)
    return RPE_index_list


# 自动分割柔顺版（无法有效分割有病灶的情况）
def get_RPE_curve_index(matrix):
    yvals_int = []
    RPE_index_list = get_PRE_index(matrix)
    x = [x for x in range(len(matrix[0]))]
    f1 = np.polyfit(x, RPE_index_list, 5)
    p1 = np.poly1d(f1)
    yvals = p1(x)
    for y in yvals:
        yvals_int.append(int(y))
    return yvals_int


# 利用金标准找到索引
def detect_RPE_curve_index(matrix):
    y_indexs = []
    temp = 180
    trigger = True
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            if matrix[x,y]:
                y_indexs.append(x)
                temp = x
                trigger=False
                break
        if trigger:
            y_indexs.append(temp)
    return y_indexs

# 根据RPE层展平
def flatten(matrix, seg, y_criterion, len_padding):
    padding = []
    for _ in range(len_padding):
        padding.append([0]*len(matrix[0]))
    zero_matrix = np.zeros_like(matrix)
    res = np.vstack((zero_matrix, padding))
    # print(res.shape)
    # print(matrix_padding.shape)
    y_indexs = detect_RPE_curve_index(seg)
    # print(y_indexs)
    for y in range(len(matrix[0])):
        diff = y_criterion - y_indexs[y]
        for x in range(len(matrix)):
            res[x+diff,y] = matrix[x,y]
    return res


if __name__ == '__main__':
    # -------------------------------
    # 读入图片
    img_array = sitk.GetArrayFromImage(sitk.ReadImage("./testset/00000215.nii.gz"))
    seg_array = sitk.GetArrayFromImage(sitk.ReadImage("./testset/seg_6.nii.gz"))
    one_seg_array = seg_array[6]
    one_img_array = img_array[6]

    # -------------------------------
    # 矩阵转图片
    # cv2.imwrite("1.jpg", one_img_array)
    # img = cv2.imread("1.jpg")
    # -------------------------------
    # 获取PRE的y方向索引
    x = [x for x in range(len(one_img_array[1]))]
    flatten_img = flatten(one_img_array, one_seg_array, 300, 200)
    fig, ax = plt.subplots()
    # img_array = plt.imread("1.jpg")
    res = flatten_img[100:-200][:]
    ax.imshow(res, cmap='gray')
    # ax.plot(x, yvals)
    plt.savefig("./testset/flatten.jpg")
    plt.show()
