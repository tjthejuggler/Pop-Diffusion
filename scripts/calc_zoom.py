import cv2
import numpy as np
import argparse
#
# import imutils

image_width, image_height = 1156,781
print('image_hor_center_pixel: ', image_width/2)
print('image_ver_center_pixel: ', image_height/2)
#left, right, top, bottom
box_coordinates = [500.7762908935547,753.3664703369141,461.3892846107483,714.9949359893799]
#box_coordinates = [0, 1156, 0, 781]
num_iterations = 30
box_width = abs(box_coordinates[0] - box_coordinates[1])
box_height = abs(box_coordinates[2] - box_coordinates[3])

if image_width/box_width > image_height/box_height:
    small_number = box_width
    large_number = image_width
else:
    small_number = box_height
    large_number = image_height 

def get_percent_increase(large_number,small_number):
    percent_increase = (large_number / small_number) ** (1/num_iterations)
    return percent_increase

percent_increase = get_percent_increase(large_number,small_number)

def calculate_box_center_pixel(box_coordinates):
    box_center_pixel_horizontal = (box_coordinates[0] + box_coordinates[1])//2
    box_center_pixel_vertical = (box_coordinates[2] + box_coordinates[3])//2
    return box_center_pixel_horizontal, box_center_pixel_vertical

box_center_pixel_hor, box_center_pixel_ver = calculate_box_center_pixel(box_coordinates)
print('box_center_pixel_hor:',box_center_pixel_hor)
print('box_center_pixel_ver:',box_center_pixel_ver)
#these two functions somehow need combined to make an actual scale and translate for each of the iterations

def calculate_box_center_after_raw_scale(box_center_pixel_horizontal,box_center_pixel_vertical,percent_increase):
    image_center_pixel_horizontal = image_width//2
    image_center_pixel_vertical = image_height//2
    hor_change = (((percent_increase-1) * image_width)//2) * num_iterations
    print('box_center_pixel_horizontal:',box_center_pixel_horizontal)
    print('image_center_pixel_horizontal:',image_center_pixel_horizontal)
    if box_center_pixel_horizontal < image_center_pixel_horizontal:
        box_center_pixel_horizontal_after_raw_scale = box_center_pixel_horizontal - hor_change
    elif box_center_pixel_horizontal > image_center_pixel_horizontal:
        box_center_pixel_horizontal_after_raw_scale = box_center_pixel_horizontal + hor_change
    else:
        box_center_pixel_horizontal_after_raw_scale = box_center_pixel_horizontal
    ver_change = (((percent_increase-1) * image_height)//2) * num_iterations
    print('box_center_pixel_vertical:',box_center_pixel_vertical)
    print('image_center_pixel_vertical:',image_center_pixel_vertical)
    if box_center_pixel_vertical < image_center_pixel_vertical:
        box_center_pixel_vertical_after_raw_scale = box_center_pixel_vertical - ver_change
    elif box_center_pixel_vertical > image_center_pixel_vertical:
        box_center_pixel_vertical_after_raw_scale = box_center_pixel_vertical + ver_change
    else:
        box_center_pixel_vertical_after_raw_scale = box_center_pixel_vertical
    return box_center_pixel_horizontal_after_raw_scale, box_center_pixel_vertical_after_raw_scale

box_center_pixel_horizontal_after_raw_scale, box_center_pixel_vertical_after_raw_scale = \
    calculate_box_center_after_raw_scale(box_center_pixel_hor, box_center_pixel_ver, percent_increase)

print('box_center_pixel_horizontal_after_raw_scale',box_center_pixel_horizontal_after_raw_scale)
print('box_center_pixel_vertical_after_raw_scale',box_center_pixel_vertical_after_raw_scale)

#figure out the hor and ver change required to get to the center of the image
hor_change_per_iteration = int(((image_width//2) - box_center_pixel_horizontal_after_raw_scale) / num_iterations)
ver_change_per_iteration = int(((image_height//2) - box_center_pixel_vertical_after_raw_scale) / num_iterations)

print('hor_change_per_iteration', hor_change_per_iteration)
print('ver_change_per_iteration', ver_change_per_iteration)
print('percent_increase', percent_increase)

#display the imagein a window
image = cv2.imread('ODimage.png')
#cv2.rectangle(image, (box_coordinates[0], box_coordinates[2]), (box_coordinates[1], box_coordinates[3]), (0, 255, 0), 2)

def zoom_center(img, zoom_factor):

    y_size = img.shape[0]
    x_size = img.shape[1]
    
    # define new boundaries
    x1 = int(0.5*x_size*(1-1/zoom_factor))
    x2 = int(x_size-0.5*x_size*(1-1/zoom_factor))
    y1 = int(0.5*y_size*(1-1/zoom_factor))
    y2 = int(y_size-0.5*y_size*(1-1/zoom_factor))

    # first crop image then scale
    img_cropped = img[y1:y2,x1:x2]
    return cv2.resize(img_cropped, None, fx=zoom_factor, fy=zoom_factor)

from PIL import Image


def zoom_at(img, x, y, zoom):
    w, h = img.shape[0]. img.shape[1]
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2, 
                    x + w / zoom2, y + h / zoom2))
    return img.resize((w, h), Image.LANCZOS)





#translate the image on the x by 5 pixels
M = np.float32([
	[1, 0, hor_change_per_iteration],
	[0, 1, ver_change_per_iteration]
])
for i in range(num_iterations):
    image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    #image = zoom_center(image, percet_increase)
    image = zoom_at(image, image_width//2, image_height//2, percent_increase)
    # cv2.imshow('image', image)
    # cv2.waitKey(0)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()








