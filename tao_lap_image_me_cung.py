import cv2
import numpy as np
W = 21
M=10
N=30
image = np.zeros((M*W, N*W,3), np.uint8)

MAP = """
##############################
#         #              #   #
# ####    ########       #   #
# o  #    #              #   #
#    ###     #####  ######   #
#      #   ###   #           #
#      #     #   #  #  #   ###
#     #####    #    #  # x   #
#              #       #     #
##############################
"""    
# Convert map to a list 
MAP = [list(x) for x in MAP.split("\n") if x]

mau_xanh   = np.zeros((W,W,3), np.uint8)+ (255,0,0)
mau_trang = np.zeros((W,W,3), np.uint8) + (255,255,255)

# vẽ bản đồ mê cung
for x in range(0, M):
    for y in range(0,N):
        if MAP[x][y] == '#':
            image[x*W:(x+1)*W,y*W:(y+1)*W,:] = mau_xanh
        else:
            image[x*W:(x+1)*W,y*W:(y+1)*W,:] = mau_trang

# vẽ điểm bắt đầu
for x in range(0, M):
    for y in range(0,N):
        if MAP[x][y]=='o':
            cv2.rectangle(image,(y*W+1,x*W+1),((y+1)*W-1,(x+1)*W-1),(255,0,255),-1)
        if MAP[x][y]=='x':
            cv2.rectangle(image,(y*W+1,x*W+1),((y+1)*W-1,(x+1)*W-1),(0,0,255),-1)

        
cv2.imshow('Image', image)
cv2.waitKey(0)

