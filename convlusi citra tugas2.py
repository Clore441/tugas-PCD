import numpy as np
import cv2

image1 = cv2.imread("C:\\Users\\a516j\\Downloads\\orange.jpeg",0)
#cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
image2= cv2.imread("C:\\Users\\a516j\\Downloads\\download (1).jpg",0)

#konvolusi manual
def konvolusi(image, kernel):
    row,col= image.shape
    mrow,mcol=kernel.shape
    h =int(mrow/2)

    canvas = np.zeros((row,col),np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            if i==0 or i==row-1 or j==col-1:
                canvas.itemset((i,j),0)
            else:
                imgsum=0
                for k in range (-h, mrow-h):
                    for l in range (-h, mcol-h):
                        res=image[i+k,j+l] * kernel[h+k,h+l]
                        imgsum+=res
                    canvas.itemset((i,j), imgsum)
    return canvas
 
def kernel1(image):
    kernel = np.array([[-1/9, -1/9, -1/9],[-1/9, 8/9, -1/9],[-1/9, -1/9, -1/9]],np.float32)
    canvas = konvolusi(image, kernel)
    return canvas

def kernel2(image):
    kernel = np.array([[0, 1/8, 0],[1/8, 1/2, 1/8],[0, 1/8, 0]],np.float32)
    canvas2 = konvolusi(image, kernel)
    return canvas2


test1=kernel1(image1)
cv2.imshow("gambar1",image1)
cv2.imshow("High pass",test1)


test2=kernel2(image2)
cv2.imshow("gambar2",image2)
cv2.imshow("low pass",test2)


print(" gamabr1 ", image1)    
print(" gambar2 ", image2)
print(" gambar1 ", image1.shape)
print(" gambar2 ", image2.shape) 
print(" high filter image1 ", test1.shape)
print(" lowpass image1", test1.shape)
print(" high filter image2 ", test2.shape)
print(" lowpass image2", test2.shape)


cv2.waitKey(0)
cv2.destroyAllWindows()

"""
 Operating System: Windows 11 Home Single Language 64-bit (10.0, Build 22631) (22621.ni_release.220506-1250)
                 Language: English (Regional Setting: English)
      System Manufacturer: ASUSTeK COMPUTER INC.
             System Model: VivoBook_ASUSLaptop X515JAB_A516JA
                     BIOS: X515JAB.307 (type: UEFI)
                Processor: Intel(R) Core(TM) i5-1035G1 CPU @ 1.00GHz (8 CPUs), ~1.2GHz
                   Memory: 4096MB RAM
      Available OS Memory: 3834MB RAM
                Page File: 4982MB used, 3972MB available
              Windows Dir: C:\WINDOWS
          DirectX Version: DirectX 12
          
          """