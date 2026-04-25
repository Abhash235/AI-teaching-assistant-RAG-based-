import whisper
import json

model= whisper.load_model("large-v2")

result=model.transcribe(audio="audios/bbb.mp3",
                        language="hi",
                        task="translate",
                        word_timestamps=False)

print(result)

# with open ("output.json","w ") as f:
#     json.dump(f,result)
