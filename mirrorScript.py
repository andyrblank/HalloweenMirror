import os
import random
from time import sleep
from gpiozero import MotionSensor

#Clear console and turn off blinking cursor
#This makes for a completely black screen behind the mirror
os.system("clear")
os.system("setterm --cursor off")

#Set motion Sensor GPIO 17
pir = MotionSensor(17)

#path where videos are located
folderPath = "/home/pi/Videos/"

#List of File Names of Videos in folder
videos = ["BC_FearTheReaper_Holl_V.mp4",
    "BC_GatheringGhouls_Holl_V.mp4",    
    "PP_StartleScare1_Wall_Spotlight_V.mp4",
    "PP_StartleScare2_Wall_Spotlight_V.mp4",
    "PP_StartleScare3_Wall_Spotlight_V.mp4"]

#VLC Command for starting the video with options
# "--quiet" Turn off all messages on the console.
# "--no-osd" No on-screen display (disables title of video from displaying)
# "-f" fullscreen
# "--autoscale" Let the video scale to fit a given window or fullscreen.
# https://wiki.videolan.org/VLC_command-line_help/
vlcCommandStart = "vlc --quiet --no-osd -f --autoscale file://"

#End of the VLC Command after the file being played.
# "vlc://quit" Close VLC after video is done
# ">/dev/null 2>&1" redirect all console output to null
vlcCommandEnd = " vlc://quit >/dev/null 2>&1"

try:  
    while True: # this will carry on until you hit CTRL+C  
        os.system("clear")
        
        #Wait for motion sensor
        pir.wait_for_motion()
        
        #Give time to look at mirror reflection
        # wait 3 seconds   
        sleep(3)

        #Get video at random from list
        video = random.choice(videos)        
        #Create command to play video by concatenating command variables.
        videoCommand = vlcCommandStart + folderPath + video + vlcCommandEnd            
        #Run VLC command from BASH Shell/Terminal
        os.system(videoCommand)
        
        #After video plays let relfection 
        #show before playing another video
        #wait 3 seconds        
        sleep(3)

        #wait for motion sensor to deactivate
        #pir.wait_for_no_motion()        

# this block will run no matter how the try block exits
finally:
    # clean up after yourself
    GPIO.cleanup()