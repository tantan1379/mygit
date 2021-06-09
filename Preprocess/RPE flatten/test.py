import numpy as np
import SimpleITK as sitk

def detect_RPE_curve_index(matrix):
    y_indexs = []
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            # print(matrix[x,y])
            if matrix[x,y]:
                y_indexs.append(x)
                break
    return y_indexs

seg_array = sitk.GetArrayFromImage(sitk.ReadImage("seg.nii.gz"))
one_seg_array = seg_array[0]
y_indexs = detect_RPE_curve_index(one_seg_array)
# one_list = one_seg_array[:,0]
# for iter,i in enumerate(one_list):
#     print(i)
#     if(i):
#         print(iter)
#         break
