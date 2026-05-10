import requests
import os
import json
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib 

# create embeddings of the text

def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed",json={
        "model":"bge-m3",
        "input":text_list
    })

    embedding= r.json()["embeddings"]
    return embedding

my_dict=[]
chunk_id=0
jsons=os.listdir("jsons") #list all the jsons

for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content=json.load(f)
        # print(f"creating embeddings for {json_file}")
        
    embeddings = create_embeddings([c["text"] for c in content["chunks"]]) # first it give a list of texts of chunk , then call the function for embedding
    for i,chunk in enumerate(content["chunks"]):
        chunk["chunk_id"] = chunk_id
        chunk["embedding"] = embeddings[i]
        chunk_id +=1
        my_dict.append(chunk)

# print(my_dict)


df = pd.DataFrame.from_records(my_dict)
# save this dataframe
joblib.dump(df,"embeddings.joblib")
# print(df)


