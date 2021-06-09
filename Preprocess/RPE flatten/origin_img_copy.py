import shutil
import SimpleITK as sitk
import xlrd
import os

num_pat = 105
des_path = "F:\\Dataset\\AMD\\AMD_Origin_3d_in_need\\"
# if not os.path.exists(des_path+""):

book = xlrd.open_workbook("./dicom_path.xlsx")
sheet = book.sheet_by_index(0)
index_list = list()
v1_list = list()
v2_list = list()
v3_list = list()
for index in sheet.col_values(0,start_rowx=1):
    if not os.path.exists(os.path.join(des_path, index)):
        os.mkdir(os.path.join(des_path, index))
    if not os.path.exists(os.path.join(des_path,index,index+"_v1")):
        os.mkdir(os.path.join(des_path,index,index+"_v1"))
    if not os.path.exists(os.path.join(des_path,index,index+"_v2")):
        os.mkdir(os.path.join(des_path,index,index+"_v2"))
    if not os.path.exists(os.path.join(des_path,index,index+"_v3")):
        os.mkdir(os.path.join(des_path,index,index+"_v3"))
    index_list.append(index)
# print(index_list)

for v1 in sheet.col_values(4,start_rowx=1):
    v1_list.append(v1)
# print(v1_list)

for v2 in sheet.col_values(6,start_rowx=1):
    v2_list.append(v2)

for v3 in sheet.col_values(8,start_rowx=1):
    v3_list.append(v3)

# print(des_path+index_list[0])
for i in range(len(index_list)):
    shutil.copyfile(v1_list[i],des_path+index_list[i]+"\\"+index_list[i]+"_v1"+"\\"+index_list[i]+"_v1.nii.gz")
    shutil.copyfile(v2_list[i],des_path+index_list[i]+"\\"+index_list[i]+"_v2"+"\\"+index_list[i]+"_v2.nii.gz")
    shutil.copyfile(v3_list[i],des_path+index_list[i]+"\\"+index_list[i]+"_v3"+"\\"+index_list[i]+"_v3.nii.gz")

