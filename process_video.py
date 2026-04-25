# convert the videos into mp3
import subprocess
import os

files =os.listdir("videos")

for file in files:
    # print(file)
    tutorial_no= file.split(".")[0].split("Tutorial")[1]
    # print(tutorial_no)
    file_name=file.split("_")[0]
    print(tutorial_no, file_name)

    subprocess.run(["ffmpeg","-i",f"videos/{file}",f"audios/{tutorial_no}_{file_name}.mp3"])

print("hello")
