
'''
For LAMWITTY project Andrea Cuadra
Programming assistance: May Dixit
Original clipping script from Nik Martelaro: https://github.com/nikmart/video-tools
'''

import os
import sys

# CONSTANTS
CUT_TIME = 0
LABEL = 4

# FUNCTIOINS
def create_clip(cut_in, cut_out, name):
    print("Cutting from {} to {}".format(cut_in, cut_out))
    # run an ffmpeg thread to create MP4 clips
    mp4 = 'ffmpeg -i ' + videoFile + ' -ss ' + \
        cut_in + \
        ' -to ' + \
        cut_out + \
        ' -c copy ' + name + '.mp4'
    print(mp4)
    os.system(mp4)

def create_image_files(cut_in, cut_out, name):
    print("Cutting from {} to {}".format(cut_in, cut_out))
    # run an ffmpeg thread to create MP4 clips
    #png = 'ffmpeg -i ' + videoFile + ' -vf fps=29,' + \
     #   'select="between(t,' + cut_in + ',' + cut_out + ')" ' + \
    #  name + '_image%d.png'
    jpg = 'ffmpeg -i ' + videoFile + ' -ss ' + cut_in + ' -to ' + cut_out + ' -vf fps=29 ' + name + '_image%d.jpg'

    print(jpg)
    os.system(jpg)


def create_clip_list():
    clips = list()
    with open(cutFile, 'r') as f:
        for line in f:
            line = line.strip().split(",")
            if "in" in line[LABEL]:
                cut_in = line[CUT_TIME]
            elif "out" in line[LABEL]:
                cut_out = line[CUT_TIME]
                # get label from the string from line[LABEL] : Get Y/ N/ O
                label = line[LABEL][0]
                clips.append((cut_in, cut_out, label))
                # add a new entry for start, end, label
            else:
                pass
    return clips

def create_clips(clips, participant):
    clip_counter = 0
    for tup in clips: 
        start = tup[0]
        end = tup[1]
        lab = tup[2]
        name = "Footage/" + lab + '/' + lab + "_" + participant + "_clip" + str(clip_counter)
        clip_counter += 1
        create_clip(start, end, name)

def create_images(clips, participant):
    clip_counter = 0
    for tup in clips: 
        start = tup[0]
        end = tup[1]
        lab = tup[2]
        name = "Images/" + lab + '/' + lab + "_" + participant + "_clip" + str(clip_counter) 
        clip_counter += 1
        create_image_files(start, end, name)

# SCRIPT
# Check for the command line inputs
images = False
if len(sys.argv) < 2:
    print("No video file or cut file given\nUsage: \
    python supercut_creator.py [videoFile] [cutFile]")
    quit()
else:
    videoFile = sys.argv[1]
    cutFile = sys.argv[2]
    if len(sys.argv) > 3 and sys.argv[3] != None:
        images = True
print(cutFile, videoFile, images)
participant = cutFile.split(".")[0]
clips = create_clip_list()
if (images):
    create_images(clips, participant)
else: 
    create_clips(clips, participant)




