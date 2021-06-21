# -*- coding: utf-8 -*-
"""
Created on Sat May 15 01:31:54 2021

@author: SauronsEye
"""

import cv2
import pygame
import numpy as np
import random
from matplotlib import pyplot as plt

originalImage = cv2.imread('map.jpg')

print(len(originalImage))
print(len(originalImage[0]))
originalImage =cv2.resize(originalImage, (0, 0), fx = 0.5, fy = 0.5)
cv2.imshow('Original',originalImage)
img2 = cv2.convertScaleAbs(originalImage, alpha=3, beta=-320)
grayImg = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
(thresh, bwImg) = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Black white image', bwImg)

windx = len(bwImg[0])
windy = len(bwImg)


        

conx = []
cony = []
allx = []
ally = []
startpos = []
endpos = []
skip =False
for x in range(0,len(bwImg)):
    for y in range(0,len(bwImg[x])):
        if([x,y] in allx):
            skip =True
        
        else:
            skip = False
        if(skip):
            print("skip")
        else:
                
            if(bwImg[x][y] == 0):
                
                ty= y+1
                tx = x
                tempx = []
                tempy = []
                endConn =False
                nocount = 0
                xflux = y
                justbreak =False
                while not endConn:
                    if(nocount>=1):
                        endConn = True
                       
                    
                    if(ty>=(len(bwImg[0])-1)):
                        ty = xflux
                        tx = tx+1
                        
                    if(tx>=(len(bwImg)-1)):
                        print("Exceed")
                        endConn = True
                    else:
                        if(bwImg[tx][ty] == 0):
                            justbreak = False
                            tempx.append(ty)
                            tempy.append(tx)
                            allx.append([tx,ty])
                            
                            
                            if(ty+1<len(bwImg[0])):
                                ty = ty+1
                        else:
                            if(tx+1<(len(bwImg))):
                                tx = tx +1
                            else:
                                endConn = True
                            ty = xflux
                            if(justbreak):
                                nocount =+ 1
                            justbreak =True;
                   
                    print(x,y,len(bwImg))
                
                if(len(tempx) != 0 and len(tempy)!=0):
                    conx.append(tempx)
                    cony.append(tempy)
                    startpos.append([x,y])
                    endpos.append([tx,ty])
            
  
pygame.init()
displayWin = pygame.display.set_mode((windx,windy))

clock = pygame.time.Clock()
windowOpen = True;

#Color Definition for Pygame
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
blue= (0,0,255)
goodx = []
goody = []
mainx = []
mainy = []    
randcol = []  

slopeMain = []
interceptMain = []
for i in range(0,len(conx)):
    xy= []
    x2 = []
    randc = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    randcol.append(randc)
    for j in range(0,len(conx[i])):
        xy.append(conx[i][j]*cony[i][j])
        x2.append(conx[i][j]**2)
        
    sumx = np.sum(conx[i])
    sumy = np.sum(cony[i])
    sumxy = np.sum(xy)
    sumx2 = np.sum(x2)
    n = len(conx)
    
    m = ((n*(sumxy)) - (sumx*sumy))/((n*(sumx2)) - (sumx**2))
    b = ((sumy)-(m*sumx))/n
    print(m,b)
    slopeMain.append(m)
    interceptMain.append(b)

while windowOpen:
      displayWin.fill(white)
      for i in range(0,len(slopeMain)):
          
          pygame.draw.line(displayWin, black, (conx[i][0],cony[i][0]), (conx[i][-1],cony[i][-1]), 1)        
         
          
      #for i in range(0,len(conx)):    
          #for j in range(0,len(conx[i])):
              #pygame.draw.circle(displayWin,randcol[i] ,(conx[i][j],cony[i][j]), 1)
      
        
      for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            windowOpen = False;
            
      pygame.display.update();
      clock.tick(30)
pygame.image.save(displayWin,"screenshot.jpg")
pygame.quit()
cv2.destroyAllWindows()            