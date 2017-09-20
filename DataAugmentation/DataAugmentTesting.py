import DataAugment
import os
import sys
import glob
import random
import cv2
import numpy as np
from matplotlib import pyplot as plt

# set data augmentation method 
# if methos = 1 -> use

DataAugmentMethod = {
	'_avg_blur' : 0,
	'_gaussain_blur' : 1,
	'_gaussain_noise' : 1, 
	'_img_shift' : 1,
	'_img_rotation' : 1,
	'_img_flip' : 0,
	'_img_zoom' : 0, 
	'_img_contrast' : 1, 
	'_img_color' : 0
}

# generate data

_generate_quantity = 100

# set the database relative path

database = './data'

# change dir to database path

os.chdir(database)

# get all of the '.jpg' file in the database path 

images = os.listdir('.')
images = glob.glob('*.jpg')

# get quantity of '.jpg' file

size = len(images)
print (size)

# check workspace

os.chdir('../')
print(os.getcwd())

# parameter for data augment functions

_max_filiter_size = 5 		#for avg_blur and gaussain_blur
_sigma = 0 					# for gaussain_blur

_mean = 0 					# for gaussain_noise
_var = 0.1					# for gaussain_noise

_x_min_shift_piexl = -20 	# for img_shift
_x_max_shift_piexl = 20 	# for img_shift
_y_min_shift_piexl = -20 	# for img_shift
_y_max_shift_piexl = 20		# for img_shift
_fill_pixel = 255			# for img_shift and img_rotation

_min_angel = -10			# for img_rotation
_max_angel = 10				# for img_rotation
_min_scale = 0.9			# for img_rotation
_max_scale = 1.1			# for img_rotation

_min_zoom_scale = 1			# for img_zoom
_max_zoom_scale = 1			# for img_zoom

_min_s = -10				# for img_contrast
_max_s = 10					# for img_contrast
_min_v = -10				# for img_contrast
_max_v = 10					# for img_contrast

_min_h = -10				# for img_color
_max_h = 10					# for img_color

DataAugmentBase = './Augment/'

for i in images:
	generate_quantity = _generate_quantity
	while generate_quantity > 0 :
		img_dir = database + '/' + i
		img = cv2.imread(img_dir)
		#print (generate_quantity)
		if DataAugmentMethod['_avg_blur'] == 1 :
			if random.randint(0, 1) == 1 :
				img = DataAugment.avg_blur(img, _max_filiter_size)
				#print ('do ab')
		if DataAugmentMethod['_gaussain_blur'] == 1 :
			if random.randint(0, 1) == 1 :
				img = DataAugment.gaussain_blur(img, _max_filiter_size, _sigma)
				#print ('do gb')
		if DataAugmentMethod['_gaussain_noise'] == 1 :
			if random.randint(0, 1) == 1 :
				img = DataAugment.gaussain_noise(img, _mean, _var)
				#print ('do gn')
		if DataAugmentMethod['_img_shift'] == 1 :
			if random.randint(0, 1) == 1 :
				img = DataAugment.img_shift(img, _x_min_shift_piexl, _x_max_shift_piexl, _y_min_shift_piexl, _y_max_shift_piexl, _fill_pixel)
				#print ('do is')
		if DataAugmentMethod['_img_rotation'] == 1 :
			if random.randint(0, 1) == 1 :
				img = DataAugment.img_rotation(img, _min_angel, _max_angel, _min_scale, _max_scale, _fill_pixel)
				#print ('do ir')
		if DataAugmentMethod['_img_flip'] == 1:
			if random.randint(0, 1) == 1 :
				img = DataAugment.img_flip(img)
				#print ('do if')
		if DataAugmentMethod['_img_zoom'] == 1:
			if random.randint(0, 1) == 1 :
				img = DataAugment.img_zoom(img, _min_zoom_scale, _max_zoom_scale)
				#print ('do iz')
		if DataAugmentMethod['_img_contrast'] == 1:
			if random.randint(0, 1) == 1 :
				img = DataAugment.img_contrast(img, _min_s, _max_s, _min_v, _max_v)
				#print ('do ic')
		if DataAugmentMethod['_img_color'] == 1:
			if random.randint(0, 1) == 1 :
				img = DataAugment.img_color(img, _min_h, _max_h)
				#print ('do ic2')
		save_dir = ('_%06d_') % (generate_quantity)
		save_dir = DataAugmentBase + save_dir + i
		generate_quantity -= 1
		img = img.astype(np.uint8)
		cv2.imwrite(save_dir, img)












