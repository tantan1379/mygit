import os
import pydicom
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 调用本地的 dicom file 
file_path = "00000013.dcm"
ds = pydicom.dcmread(file_path)
data_element = ds.data_element("PatientsName")
pixel_bytes = ds.PixelData
pix = ds.pixel_array
img = Image.fromarray(pix[0].astype(np.uint8))
print(img)
# plt.figure()
# plt.subplot(1,2,1),plt.imshow(img,'gray')
# plt.subplot(1,2,2),plt.imshow(img1,'gray')
# plt.show()