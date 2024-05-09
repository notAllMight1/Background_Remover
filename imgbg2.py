##Import the followings

import cv2
import numpy as np
from rembg import remove 
from PIL import Image 
  
inp =  "D:\misc\Programming\python projects\Background remover\Logo.png" ##Enter your paths here and all the places where paths are needed.
outp = "D:\misc\Programming\python projects\Background remover\LogoNew1.png"
  
og_img = Image.open(inp) 
alt_img = remove(og_img) 
alt_img.save(outp) 

inp = r"D:\misc\Programming\python projects\Background remover\LogoNew1.png"
outp = r"D:\misc\Programming\python projects\Background remover\LogoNew2.png"

img = cv2.imread(inp)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) ##Converting the img to greyscale
TreshVal, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV) ##Pixels with val>=240 becomes black and val<240 becomes white
result = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite(outp, result)

inp =  "D:\misc\Programming\python projects\Background remover\LogoNew2.png"
outp = "D:\misc\Programming\python projects\Background remover\Finallogo.png"
  
og_img = Image.open(inp) 
alt_img = remove(og_img) 
alt_img.save(outp)
