import requests


def create_embeddings(text):
    r = requests.port("http://localhost:11434/api/embeddings",json={
        "model":"bge-m3",
        "prompt":text
    })

    embedding=r.json()["embedding"]
    return embedding


a = create_embeddings("cat sat on the mat")
print(a)
