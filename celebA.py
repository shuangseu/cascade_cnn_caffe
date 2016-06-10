import dlib
import cv2
import os
import time
##pos_04 celebA face 
## dlib face detector 
## else landmark+offset
detector=dlib.get_frontal_face_detector() # Load dlib's face detector
path1 ="/home/gavinpan/workspace/dataset/CelebA/"
save_dir = "/home/gavinpan/workspace/face_data/pos/pos_04"         # file to save cropped faces
path2 ="img_celeba/"
file_path = path1+"list_landmarks_celeba.txt"
img_dir =path1+path2
fp = open(file_path, "r")
data1 = fp.readlines()
fp.close()
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
save_file_number=0
err_detect=0
for i,line in enumerate(data1):
  if(i>=2):
    if i % 1000 == 0:
        print "Processing rect number " + str(i)
    parsed_line = line.split()
    path4 = parsed_line[0].strip()
    #print path4
    imgpath = img_dir+path4
    #print imgpath
    img1=cv2.imread(imgpath)
    #lefteye_x lefteye_y righteye_x righteye_y nose_x nose_y leftmouth_x leftmouth_y rightmouth_x rightmouth_y
    lex = int(parsed_line[1])
    ley = int(parsed_line[2])
    rex = int(parsed_line[3])
    rey = int(parsed_line[4])

    nx = int(parsed_line[5])
    ny = int(parsed_line[6])
    
    lmx = int(parsed_line[7])
    lmy = int(parsed_line[8])

    rmx = int(parsed_line[9])
    rmy = int(parsed_line[10])

    xmin= min(min(min(min(lex,rex),nx),lmx),rmx);
    xmax= max(max(max(max(lex,rex),nx),lmx),rmx);

    ymin= min(min(min(min(ley,rey),ny),lmy),rmy);
    ymax= max(max(max(max(ley,rey),ny),lmy),rmy);
    #print xmin,xmax,ymin,ymax
    rects = detector(img1, 1)
    if len(rects) == 0:
        bbox=[-1,-1,-1,-1];
    for j in xrange(len(rects)):
       l_t=[rects[j].left(),rects[j].top()]
       r_b=[rects[j].right(),rects[j].bottom()]
       #print l_t
       #print r_b
       if(xmin>l_t[0] and ymin>l_t[1] and xmax<r_b[0] and ymax<r_b[1]):
           bbox=[rects[j].top(),rects[j].bottom(),rects[j].left(),rects[j].right()]
           break;
       else:
           bbox=[-1,-1,-1,-1];
    if(bbox[0]!=-1):
        cropped_img = img1[bbox[0]:bbox[1],bbox[2]:bbox[3]]
    else:
        h=ymax-ymin
        w=xmax-xmin
        y1=int(max(ymin-0.25*h,0))
        x1=int(max(xmin-0.25*w,0))
        y2=int(min(ymax+0.25*h,img1.shape[0]-1))
        x2=int(min(xmax+0.25*w,img1.shape[1]-1))
        cropped_img = img1[y1:y2,x1:x2] 
        err_detect+=1  
    
    #print bbox
    '''
    color = (255,0,0)
    cv2.rectangle(img1,(bbox[2],bbox[0]),(bbox[3],bbox[1]), color)
    cv2.circle(img1,(lex,ley), 3, color=(0, 255, 255))
    cv2.circle(img1,(rex,rey), 3, color=(0, 255, 255))
    cv2.circle(img1,(nx,ny), 3, color=(0, 255, 255))
    cv2.circle(img1,(lmx,lmy), 3, color=(0, 255, 255))
    cv2.circle(img1,(rmx,rmy), 3, color=(0, 255, 255))
    cv2.imshow('img', img1)
    cv2.waitKey(0)
    '''
    file_name = save_dir + "/pos04_" + str(save_file_number).zfill(6) + ".jpg"
    save_file_number += 1
    cv2.imwrite(file_name, cropped_img)
print err_detect
print "end"
