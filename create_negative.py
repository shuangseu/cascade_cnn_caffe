import numpy as np
import cv2
import os
import time 
import math

data_base_dir = "/home/gavinpan/workspace/Face_detection/bg"     # file containing pictures
start_neg_dir = 1
end_neg_dir = 50
file_list = []      # list of strings storing names of pictures

for file in os.listdir(data_base_dir):
    if file.endswith(".jpg"):
        file_list.append(file)

number_of_pictures = len(file_list)     # 17723 pictures
print number_of_pictures
neg_per_file= math.ceil(number_of_pictures/end_neg_dir)
print neg_per_file
#time.sleep(1000)
# ============== create directories ==================================
directory = '/home/gavinpan/workspace/face_data/neg/neg_'    # start of path

for cur_file in range(start_neg_dir, end_neg_dir + 1):
    path = directory + str(cur_file).zfill(2)
    if not os.path.exists(path):
        os.makedirs(path)
# ============== create negatives =====================================
for current_neg_dir in range(start_neg_dir, end_neg_dir + 1):
    save_image_number = 0
    save_dir_neg = "/home/gavinpan/workspace/face_data/neg/neg_" + str(current_neg_dir).zfill(2)    # file to save patches

    for current_image in range((current_neg_dir - 1)*int(neg_per_file), (current_neg_dir - 1)*int(neg_per_file) + int(neg_per_file)):    # take  images
        if current_image % 100 == 0:
            print "Processing image number " + str(current_image)
        read_img_name = data_base_dir + '/' + file_list[current_image].strip()
        img = cv2.imread(read_img_name)     # read image
        if img is None:
            print read_img_name
            break
        height, width, channels = img.shape

        crop_size = min(height, width) / 2  # start from half of shorter side

        while crop_size >= 12:
            for start_height in range(0, height,100):
                for start_width in range(0, width,100):
                    if (start_width + crop_size) > width:
                        break
                    cropped_img = img[start_height : start_height + crop_size, start_width : start_width + crop_size]
                    file_name = save_dir_neg + "/neg" + str(current_neg_dir).zfill(2) + "_" + str(save_image_number).zfill(6) + ".jpg"
                    cv2.imwrite(file_name, cropped_img)
                    save_image_number += 1
            crop_size *= 0.5

        if current_image == (number_of_pictures - 1):
            break



