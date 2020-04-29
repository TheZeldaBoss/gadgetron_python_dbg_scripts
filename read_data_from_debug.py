import nibabel as nib
import os
from nibabel.analyze import AnalyzeHeader
import matplotlib.pyplot as plt
import time
import numpy as np

from ismrmrdtools import show, transform



def get_number_of_stacks(folder, name):
    compteur = 0
    # print(folder)
    for file in os.listdir(folder + "/"):
        if (file.startswith(name)):
            if (file.endswith("_MAG.img")):
                print(os.path.join(folder, file))
                compteur = compteur + 1;
    number_of_stacks = compteur
    return number_of_stacks


def read_real_imaginary_part(folder, name):
    #number_of_stacks = get_number_of_stacks(folder, name)

    filename = folder + name  + "_REAL.hdr"
    hdr = nib.load(filename)

    list_of_cplx = list()
    
    filename_real = folder + name  + "_REAL.img"
    filename_imag = folder + name  + "_IMAG.img"

    if (os.path.isfile(filename_real) and os.path.isfile(filename_imag)):
            print(filename_real, " - ", filename_imag)
            analyze_img_real = nib.load(filename_real)
            analyze_img_imag = nib.load(filename_imag)
           
            data_real = analyze_img_real.get_data()
            data_imag = analyze_img_imag.get_data()
            print(data_real.shape)
            print(data_imag.shape)
            
            array_real = np.asarray(data_real)
            array_imag = np.asarray(data_imag)
            array_cplx = np.zeros(data_real.shape, dtype=np.complex_, order='F')
            array_cplx = array_real + 1j * array_imag
           
    else:
            print("pb reading:", filename_real, " - ", filename_imag)

    
    return array_cplx






def display(kspace_data, image):
	plt.figure(1)
	plt.subplot(2, 4, 1)
	plt.imshow(np.abs(kspace_data), cmap="gray")
	plt.title("frequence magnitude")
	plt.subplot(2, 4, 2)
	plt.imshow(np.angle(kspace_data), cmap="gray")
	plt.title("frequence phase")
	plt.subplot(2, 4, 3)
	plt.imshow(np.abs(image), cmap="gray")
	plt.title("image magnitude")
	plt.subplot(2, 4, 4)
	plt.imshow(np.angle(image), cmap="gray")
	plt.title("image phase")
	plt.show()

def comparaison( kspace_data , kspace_data2):
	plt.figure(2)
	plt.subplot(2, 3, 1)
	plt.imshow(np.abs(kspace_data), cmap="gray")
	plt.title("frequence magnitude memcpy")
	plt.subplot(2, 3, 2)
	plt.imshow(np.abs(kspace_data2), cmap="gray")
	plt.title("frequence magnitude sed::copy")
	plt.subplot(2, 3, 3)
	plt.imshow(np.abs(kspace_data) - np.abs(kspace_data2), cmap="gray")
	diff_abs = np.abs(kspace_data) - np.abs(kspace_data2)
	a = diff_abs.sum()
	plt.title(str("{0:.9f}".format(a)))
	plt.subplot(2, 3, 4)
	plt.imshow(np.angle(kspace_data), cmap="gray")
	plt.title("frequence magnitude memcpy")
	plt.subplot(2, 3, 5)
	plt.imshow(np.angle(kspace_data2), cmap="gray")
	plt.title("frequence magnitude std::copy")
	plt.subplot(2, 3, 6)
	plt.imshow(np.angle(kspace_data) - np.angle(kspace_data2), cmap="gray")
	diff_angle = np.angle(kspace_data) - np.angle(kspace_data2)
	a = diff_angle.sum()
	plt.title(str("{0:.9f}".format(a)))
	plt.show()

folder = "/home/benoit/Documents/IHUBordeaux/test_sms_4/out/"
name = "donnee_mb_apres_extract_memcpy"
name2 = "donnee_sb_apres_extract_memcpy"


print(folder + name)
ref_coil_map = read_real_imaginary_part(folder, name)
ref_coil_map2 = read_real_imaginary_part(folder, name2)

dims=(ref_coil_map.shape)
dims2 = (ref_coil_map2.shape)
print(dims)
print(dims2)

cha=0
slc=0

kspace_data=ref_coil_map[:, :, 0, cha, 0,0, slc]
kspace_data2 = ref_coil_map2[:, :, 0, cha, 0,0, slc]

image = transform.transform_image_to_kspace(kspace_data,dim=(0,1))
image2 = transform.transform_image_to_kspace(kspace_data2, dim=(0, 1))


display(kspace_data2, image2)
display(kspace_data, image)
#comparaison(kspace_data, kspace_data2)

