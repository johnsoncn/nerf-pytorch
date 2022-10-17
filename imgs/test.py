# -*- coding: utf-8 -*-
""" 
@Time    : 2022/10/14 14:30
@Author  : Johnson
@FileName: test.py
"""

# 深度图对应的尺度因子factor 是深度图中存储的值与真实深度（单位为m）的比例
depth_image = [[],[],[]]
depth_image.height = 8
depth_image.width = 8

fx = 525.0  # focal length x
fy = 525.0  # focal length y
cx = 319.5  # optical center x
cy = 239.5  # optical center y

factor = 5000  # for the 16-bit PNG files
# OR: factor = 1 # for the 32-bit float images in the ROS bag files

for v in range(depth_image.height):
    for u in range(depth_image.width):
        Z = depth_image[v, u] / factor
        X = (u - cx) * Z / fx
        Y = (v - cy) * Z / fy

print(X,Y,Z)