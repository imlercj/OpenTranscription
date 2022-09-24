import whisper
from config import *

model = whisper.load_model("base")
result = model.transcribe("data/frac.wav")
with open('data/frac.txt','w') as f:
    f.write(result["text"])
print(result["text"])