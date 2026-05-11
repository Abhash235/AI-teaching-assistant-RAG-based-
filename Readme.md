# How to use RAG AI Teaching assistant on your own data

## step1- collect your videos
Move all your video files to video folder

## step2-  Conert ot mp3
Convert all your video files to mp3 by running video_to_mp3 

## step3 Convert mp3 to jsons
Convert all your mp3 files to json by running mp3 to json

## step4 convert json to vectors
use the file preprocess_json.py to convert the json file to a dataframe with embeddings and save it as a joblib pickel

## step5  Prompt generation and feeding to LLM
Read the joblib file and load it into the memory.Then create a relevent query as per the user and feed it to the LLM

