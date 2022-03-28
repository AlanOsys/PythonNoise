#################################################
#Welcome, everything is explained as comments :)
#################################################



import numpy as np
import pygame
import random
import math
import time
pygame.init()
random.seed(3)
count = 62500#how many squares
sqrt = round(math.sqrt(count))
noise = np.zeros(count)
noise = noise.reshape(sqrt,sqrt)
###########################

density = 350#affects clumps of similarly shaded areas(the higher the bigger the clumps)
elevation = 7#affects color definition(the higher the darker)
waterCave = 1 #affects the white clumps(the higher the bigger the white clumps) which affects water spread

#Elevation should always be at least 4, at 50+ it looks all the same, unnatural
#Cool combos:
#waterCave should only be changed if you want huge bodies of water which look connected
#anything above 2(sometimes even 1) makes weird procGens
#if elevation < 7: density > 250
#density x,elevation 4
#density 200, elevation 5
#density 200, elevation 10+ (standard)
#density 100, elevation 10+

###########################


for i in range(sqrt-1):
    for j in range(sqrt-1):
        
        value = noise[i][j] + random.uniform(-density*waterCave,density*waterCave)#changes in elevation in terms of density
        if value > 255:
            value = value/elevation
        if value < 0:
            value = value/-elevation
        #########################
        #This changes all the squares around the point you are currently looped on
        noise[i-1][j-1] += value

        noise[i][j-1] += value

        noise[i+1][j-1] += value

        noise[i-1][j] += value

        noise[i+1][j] += value

        noise[i][j] += value

        noise[i-1][j+1] += value

        noise[i][j+1] += value

        noise[i+1][j+1] += value
    
        ############################
WIDTH, HEIGHT = 1000, 700#size of display(can be changed but remember to change count value)
WIN = pygame.display.set_mode((WIDTH,HEIGHT))



def show_noise():
    for i in range(sqrt):#loops through each square to make sure elevation doesnt exceed 255
        for j in range(sqrt):
            noise[i][j] = (255 - abs(noise[i][j]))
            
            if(noise[i][j] < 0):
                noise[i][j] = abs(noise[i][j])/5
            if(noise[i][j] > 255):
                noise[i][j] = 250
            color = (noise[i][j],noise[i][j],noise[i][j])#after formating elevation we add color
            
            
            
            

            pygame.draw.rect(WIN, color, pygame.Rect(i*6, j*6, i+6, j+6))#draws the squres
def proced_gen_example():
    for i in range(sqrt):#loops through each square to make sure elevation doesnt exceed 255
        
        for j in range(sqrt):
            #Color values might have to adjusted depending on your density and elevation


            noise[i][j] = (255 - abs(noise[i][j]))
            
            if(noise[i][j] < 0):
                noise[i][j] = abs(noise[i][j])/5
            if(noise[i][j] > 255):
                noise[i][j] = 250
            if(noise[i][j] < 50):
                color = (0,0,100+noise[i][j])#Water Color
                
            elif noise[i][j] < 125 and noise[i][j] > 50:
                color = (noise[i][j]+20,noise[i][j]+20,0)#Sand Color
                
            elif noise[i][j] > 125:
                color = (0,(255-noise[i][j]),noise[i][j]-125)#Grass Color

            
            
            
            
            
            

            pygame.draw.rect(WIN, color, pygame.Rect(i*6, j*6, i+6, j+6))#draws the squres
#show_noise() #black and white spectrum
proced_gen_example() #Colors
print(noise.reshape(count))#This variable is an array of all points on the grid
##it can be used for procedural generation in other code by refering to it

while True:#pygame Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()

