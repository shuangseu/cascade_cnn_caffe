# cascade_cnn_caffe
Thanks for anson0910's code [https://github.com/anson0910/CNN_face_detection] and I modify it and fix some bugs
based on the paper Li et al., “A Convolutional Neural Network Cascade for Face Detection, ” 2015 CVPR

I follow this and train model
1.download face and non-face dataset
2.create negative patches by running create_negative.py with data_base_dir modified to the folder containing the negative images 
3.Create positive patches by running aflw.py
4.run shuffle_write_positives.py and shuffle_write_negatives.py to shuffle and write position and labels of images to file.
5.run write_train_val.py to create train.txt, val.txt and move images to corresponding folders as caffe requires.
6.use create_12_net_data.sh to create lmdb files as caffe requires.
7.start training by train_12_net.sh
