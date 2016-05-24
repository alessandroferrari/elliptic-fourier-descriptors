'''
Created on Jan 7, 2013

@author: Alessandro Ferrari

Test unit
'''

import cv2
import cv2.cv as cv
import numpy as np
import os

from elliptic_fourier_descriptors import *

testdir = os.path.join("/tmp")

test_shape1 = np.array([[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [ 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
              [ 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
              [ 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
              [ 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
              [ 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
              [ 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],], np.uint8)*255
test_shape2 = np.array([[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [ 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
              [ 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
              [ 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
              [ 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
              [ 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
              [ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],],np.uint8)*255
test_shape3 = np.array([[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [ 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
              [ 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
              [ 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
              [ 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
              [ 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],], np.uint8)*255


N = 10

#efds1 is a 3D array, 1st dim indexes different segments in the image,
#2nd dim indexes descriptors order, while 3d dimension is to access 
#the 4 different coefficients for each efd order
efds1, K1, T1 = elliptic_fourier_descriptors(test_shape1,N)

print "shape 1 \n {0}".format(efds1)

efds2, K2, T2 = elliptic_fourier_descriptors(test_shape2,N)

print "shape 2 \n {0}".format(efds2)

efds3, K3, T3 = elliptic_fourier_descriptors(test_shape3,N)

print "shape 3 \n {0}".format(efds3)

#reconstruct the first shape
if T1 != 0:
    #access the first (and only) segment
    rec1 = reconstruct(efds1[0,:],T1[0],K1[0])
    #scale to a fixed size for display purposes
    rec1[:,0] = rec1[:,0] - np.min(rec1[:,0])
    rec1[:,1] = rec1[:,1] - np.min(rec1[:,1])
    max_rec1 = np.max(rec1[:,0])
    rec1 = rec1 / max_rec1 * 100
else:
    rec1 = np.array([[0,0]])

#reconstruct the second shape
if T2 != 0:
    #access the first (and only) segment
    rec2 = reconstruct(efds2[0,:],T2[0],K2[0])
    #scale to a fixed size for display purposes
    rec2[:,0] = rec2[:,0] - np.min(rec2[:,0])
    rec2[:,1] = rec2[:,1] - np.min(rec2[:,1])
    max_rec2 = np.max(rec2[:,0])
    rec2 = rec2 / max_rec2 * 100
else:
    rec2 = np.array([[0,0]])

#reconstruct the third shape
if T3 != 0:
    #access the first (and only) segment 
    rec3 = reconstruct(efds3[0,:],T3[0],K3[0])
    #scale to a fixed size for display purposes
    rec3[:,0] = rec3[:,0] - np.min(rec3[:,0])
    rec3[:,1] = rec3[:,1] - np.min(rec3[:,1])
    max_rec3 = np.max(rec3[:,0])
    rec3 = rec3 / max_rec3 * 100
else:
    rec3 = np.array([[0,0]])

max_tot = max(np.max(rec1), np.max(rec2), np.max(rec3))

img1 = np.zeros((max_tot+10,max_tot+10))
img2 = np.zeros((max_tot+10,max_tot+10))
img3 = np.zeros((max_tot+10,max_tot+10))

for i in range(len(rec1)):
    img1[int(rec1[i,0]), int(rec1[i,1])] = 255

for i in range(len(rec2)):
    img2[int(rec2[i,0]), int(rec2[i,1])] = 255
    
for i in range(len(rec3)):
    img3[int(rec3[i,0]), int(rec3[i,1])] = 255
    
cv2.imwrite(os.path.join(testdir, "rec1.png"), img1)
cv2.imwrite(os.path.join(testdir, "rec2.png"), img2)
cv2.imwrite(os.path.join(testdir, "rec3.png"), img3)
