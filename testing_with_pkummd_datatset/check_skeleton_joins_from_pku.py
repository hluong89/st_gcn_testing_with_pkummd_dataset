
# this Python file do the following tasks:
# read a video
# extract frames from video
# plot skeleton joints from a given file to a new frame

import numpy as np
import cv2

def slip_frame_from_video():
    cap = cv2.VideoCapture('0024-M.avi')
    ret, frame = cap.read()

    count = 0

    while ret and count < 5:
        cv2.imwrite('frame{}.jpg'.format(count), frame)
        ret, frame = cap.read()
        print('Reading a new frame: ')
        count += 1

#slip_frame_from_video()
print('Done!')

max_person = 2
number_of_joint = 25
number_of_dimension = 3

def read_skeleton_info():
    # read skeleton information of the first frame
    f = open('0024-M.txt', 'r')
    first_line = f.readline()
    coordinate = first_line.split()
    skeleton = []
    count = 0
    for i in coordinate:
        if count < number_of_joint * number_of_dimension:
            skeleton.append(float(i))
        else:
            break
    return skeleton

# This file plots skeleton joints provided by PKU to a new frame obtained from the video
# def plot_skeleton_join(namefile):
#     img = cv2.imread(namefile)
#     #h, w, c = img.shape
#     h = np.size(img, 0)
#     w = np.size(img, 1)
#     c = np.size(img, 2)
#     print(h,w,c)
#
#     skeleton = read_skeleton_info()
#     i = 0
#     count = 0
#     while(i< (len(skeleton)-2)):
#         x = skeleton[i]
#         y = skeleton[i+1]
#         z = skeleton[i+2]
#
#         print(x,y,z)
#         # x_c = abs(int(h * x))
#         # y_c = abs(int(w * y))
#
#         # Assume that after normalise data (x,y), (x,y) belong to (-1,1)
#         x = x / 2 + 0.5
#         y = y / 2 + 0.5
#
#         x_c = int(w * x)
#         y_c = int(h * y)
#
#         cv2.circle(img, (x_c, y_c), 5, (0, 255, 0), thickness=2, lineType=cv2.FILLED)
#         cv2.putText(img, "{}".format(count), (x_c, y_c), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1,
#                     lineType=cv2.LINE_AA)
#         count = count + 1
#         i = i + 3
#
#
#     cv2.imshow('Test image', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#     # x_1 = float(skeleton[0])
#     # print((type(x_1)))
#     # y_1 = float(skeleton[1])
#     # z = float(skeleton[2])
#     # print(x_1, y_1, z)
#     #
#     # h_c_1 =  abs(int(h * x_1))
#     # w_c_1 = abs(int(w * y_1))
#     # cv2.circle(img, (h_c_1, w_c_1), 25, (0, 255, 0), 5)
#     #
#     # cv2.imshow('Test image', img)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()


def plot_skeleton_join(namefile):
    img = cv2.imread(namefile)
    #h, w, c = img.shape
    h = np.size(img, 0)
    w = np.size(img, 1)
    c = np.size(img, 2)
    print(h,w,c)

    skeleton = read_skeleton_info()
    i = 0
    count = 0
    while(i< (len(skeleton)-2)):
        x = skeleton[i]
        y = skeleton[i+1]
        z = skeleton[i+2]

        print(x,y,z)
        # x_c = abs(int(h * x))
        # y_c = abs(int(w * y))
        # x = x * 1920
        # y = y * 1080
        # Assume that after normalise data (x,y), (x,y) belong to (-1,1)
        x = x / 4 + 0.5
        y = -y / 2.5 + 0.5

        x_c = int(w * x)
        y_c = int(h * y)

        cv2.circle(img, (x_c, y_c), 8, (0, 255, 0), thickness=2, lineType=cv2.FILLED)
        cv2.putText(img, "{}".format(count), (x_c, y_c), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                    lineType=cv2.LINE_AA)
        count = count + 1
        i = i + 3


    cv2.imshow('Test image', cv2.resize(img, (640,480)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # x_1 = float(skeleton[0])
    # print((type(x_1)))
    # y_1 = float(skeleton[1])
    # z = float(skeleton[2])
    # print(x_1, y_1, z)
    #
    # h_c_1 =  abs(int(h * x_1))
    # w_c_1 = abs(int(w * y_1))
    # cv2.circle(img, (h_c_1, w_c_1), 25, (0, 255, 0), 5)
    #
    # cv2.imshow('Test image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



plot_skeleton_join('frame0.jpg')








