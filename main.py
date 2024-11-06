import whisper

model = whisper.load_model("base")
result = model.transcribe("seu_video.mp4")
with open("legenda.txt", "w") as f:
    f.write(result["text"])
