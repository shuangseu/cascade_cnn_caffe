import cv2
import os
## wider face pos_02 train
##            pos_03 val
path1 ="/home/gavinpan/workspace/dataset/wider_face/"
#save_dir = "/home/gavinpan/workspace/face_data/pos/pos_02"         # file to save cropped faces
save_dir = "/home/gavinpan/workspace/face_data/pos/pos_03"         # file to save cropped faces
#path2 ="WIDER_train/images/"
path2 ="WIDER_val/images/"
#file_path = path1+"wider_face_train.txt"
file_path = path1+"wider_face_val.txt"
img_dir =path1+path2
fp = open(file_path, "r")
data1 = fp.readlines()
fp.close()
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
save_file_number=0
for i,line in enumerate(data1):
    if i % 1000 == 0:
        print "Processing rect number " + str(i)
    parsed_line = line.split()
    path4 = parsed_line[0].strip()
    #print path4
    imgpath = img_dir+path4
    #print imgpath
    img1=cv2.imread(imgpath)
    x = int(parsed_line[1])
    y = int(parsed_line[2])
    w = int(parsed_line[3])
    h = int(parsed_line[4])

    #color = (255,0,0)
    #cv2.rectangle(img1, (x, y), (x+w, y+h), color)
    #cv2.imshow('img', img1)
    #cv2.waitKey(1)
    if(w>12 and h>12):
        cropped_img = img1[y : y + h, x : x + w]
        #file_name = save_dir + "/pos02_" + str(save_file_number).zfill(6) + ".jpg"
        file_name = save_dir + "/pos03_" + str(save_file_number).zfill(6) + ".jpg"
        save_file_number += 1
        cv2.imwrite(file_name, cropped_img)
print "end"
