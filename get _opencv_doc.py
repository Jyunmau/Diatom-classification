import sys
import cv2

out = sys.stdout
sys.stdout = open("help_cv2.md", "w")

help(cv2)

sys.stdout.close()
sys.stdout = out
