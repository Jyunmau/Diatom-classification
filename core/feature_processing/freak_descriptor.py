import cv2

image = None
keypoints = None
freakExtractor = cv2.xfeatures2d.FREAK_create()
keypoints, descriptors = freakExtractor.compute(image, keypoints)
