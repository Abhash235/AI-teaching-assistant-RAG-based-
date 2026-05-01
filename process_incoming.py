import requests
import os
import json
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib 


def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed",json={
        "model":"bge-m3",
        "input":text_list
    })

    embedding= r.json()["embeddings"]
    return embedding

    
df=joblib.load("embeddings.joblib")

incoming_query=input("Ask a question :")
quesiton_embeddings=create_embeddings([incoming_query])[0]
# print(quesiton_embeddings)


# find the similaritis of quesiotn_embeddings and other embeddings

# here the embedding is converted into 2D by np.vstack() , cosine_similarity takes 2D vectors
similaritis=cosine_similarity(np.vstack(df["embedding"]),[quesiton_embeddings]).flatten()
# print(similaritis)
# print(similaritis.argsort())


# used to get top 3 result
top_result=3
max_index=similaritis.argsort()[::-1][0:top_result]
# print(max_index)

new_df=df.loc[max_index]
print(new_df[["number","title","text"]])

prompt = f''' im teaching web devlopment using sigma web devlopment course. Here are videos chunks subtitles containing video
title, video number, start time in second , end time in second ,the text at that time:

{new_df[["title","number","start","end","text"]].to_json()}
______________________________
"{incoming_query}"
user asked this question related to the video chunks , you have to answer whwre and how much contents in taught in which 
video (in which video and at what time stamp) and guide to the user to go to the perticular video . if user asks unrelated 
question , tell him that you can only answer questions related to the course
'''

with open("prompt.txt", "w") as f:
    f.write(prompt)

# for index,item in new_df.iterrows():
#     print(index,item["number"],item["title"],item["text"])



print("complete")