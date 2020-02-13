#!/usr/bin python3.
# pip3 install moviepy

import sys


#input file
input_file = sys.argv[1]
#the time in seconds want to skip for intro
intro = sys.argv[2]
#the time in seconds where the credits start before the end
less = sys.argv[3]
#convert to floats for compatiblity
skip2 = float(less)
skip1 = float(intro)

from moviepy.editor import VideoFileClip
clip = VideoFileClip(input_file)


outro = clip.duration - skip2


print(00.00,    skip1,    3) 
print(outro,    clip.duration,    3)
        
