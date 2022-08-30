#IMPORTING LIBRARIES
import cv2

#LOADING IMAGE
img = cv2.imread("Task2.png")

#Converting Image into Gray Image
grey_filter = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#writing our GRAYImage as STEP 1
cv2.imwrite("1_Task2_GrayImageOutput.png",grey_filter)

#Inverting the Image
invert = cv2.bitwise_not(grey_filter)

#writing our INVERTED Image as STEP 2
cv2.imwrite("2_Task2_InvertedImageOutput.png",invert)

#Blurring the Image using Gaussian Blur
blur = cv2.GaussianBlur(invert,(21,21),0)

#writing our BLURRING Image as STEP 3
cv2.imwrite("3_Task2_BlurringImageOutput.png",blur)

#Inverting the Image to get the Final Sketch
invertedblur = cv2.bitwise_not(blur)

#writing our INVERTEDBLUR Image for final sketch as STEP 4
cv2.imwrite("4_Task2_InvertedBlurOutput.png",invertedblur)

sketch_filter = cv2.divide(grey_filter,invertedblur,scale=256.0)

#Writing Final Output as pencil sketch
cv2.imwrite("5_Task2_Final_Output.png",sketch_filter)