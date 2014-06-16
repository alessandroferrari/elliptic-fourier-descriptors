elliptic-fourier-descriptors
============================

Fast python/numpy/opencv implementation of the elliptic fourier descriptors for shapes recognition.

The implementation is inspired at the original work "Elliptic Fourier Features of a Closed Contour", Frank P. Kuhl, Charles Giardina, 1981. It implements both features extraction and shape reconstruction.
The function for extracting features takes as input a 2D binary image, return an array containing elliptic fourier descriptors for all segments in the image. The efds are order in raster scan sorting of the binary image, (thus, like as all the most common image labeling functions availables).
