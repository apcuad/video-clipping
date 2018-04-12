# video-clipping

#####Setup
brew install ffmpeg
Check you've got Python already 


#####Video clips

To create video clips, create directory called Footage with 3 directories inside named Y, N, and O and then run:

python supercut_creator.py [Movie file] [Annotation csv file]

Exampled:
python supercut_creator.py Marielos.MOV marielos.csv 





#####Images from video clips

To create images, create directory called Images with 3 directories inside named Y, N, and O and then run:

python supercut_creator.py [Movie file] [Annotation csv file] true

Exampled:
python supercut_creator.py Marielos.MOV marielos.csv true
