################################################################################
# Aaron Penne
# https://github.com/aaronpenne
################################################################################

import datetime
import string
import sys
from random import shuffle, seed

import helper

################################################################################
# Global variables
################################################################################

random_seed = int(random(0, 10000))
random_seed = helper.get_seed(random_seed)
helper.set_seed(random_seed)

# Get time
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

# Parameters for draw speed
frame_rate = 30

################################################################################
# Knobs to turn
################################################################################

# Canvas size
w = 1000  # width
h = 1000  # height

opacity = 3

divisions = 6

a_step = PI/100
angles_1 = helper.range_float(0, 3*(TWO_PI+a_step), a_step)
angles_2 = helper.range_float(0+TWO_PI/3, 3*(TWO_PI+TWO_PI/3+a_step), a_step)
angles_3 = helper.range_float(0+2*TWO_PI/3, 3*(TWO_PI+2*TWO_PI/3+a_step), a_step)

angles_1 = [random(x, x+a_step) for x in angles_1]
angles_2 = [random(x, x+a_step) for x in angles_2]
angles_3 = [random(x, x+a_step) for x in angles_3]

################################################################################
# setup()
# function gets run once at start of program
################################################################################

def setup():
    # Sets size of canvas in pixels (must be first line)
    size(w, h, P3D)

    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity())  # 1 for low, 2 for high

    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(HSB, 360, 100, 100, 100)

    # Set the number of frames per second to display
    frameRate(frame_rate)
    
    background(0, 0, 25)
    
    # Stops draw() from running in an infinite loop (should be last line)
    #noLoop()  # Comment to run draw() infinitely (or until 'count' hits limit)


################################################################################
# draw()
# function gets run repeatedly (unless noLoop() called in setup())
################################################################################

def draw():
    
    count = (frameCount)
    background(0, 0, 20)
    
    directionalLight(0, 0, 95, 0, 0, -10)
    ambientLight(0, 0, 50)
    
    stroke(0, 0, 20)
    fill_dark = 107
    translate(-500, -500, 950)
    for z in range(0, 10):
        fill_dark -= 9
        fill(0, 0, fill_dark)
        translate(0, 0, -500)
        for x in range(-3*w, 2*w, 300):
            for y in range(-3*h, 2*h, 300):
                # Circles
                ellipse(x+count, y+count, 30, 30)
                
                # Spheres
                # pushMatrix()
                # translate(x+count, y+count)
                # sphere(30)
                # popMatrix()
        
            
    #helper.save_frame_timestamp('grid_lights', timestamp, random_seed)

    # Save memory by closing image, just look at it in the file system
    # if (w > 1000) or (h > 1000):
    #     exit()


################################################################################
# Functions
################################################################################

def mousePressed():
    helper.save_frame_timestamp('fuzz', timestamp, random_seed)
