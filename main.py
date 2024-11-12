import whisper
def transcrever_video(arquivo_mp4):
    modelo = whisper.load_model("base")
    resultado = modelo.transcribe(arquivo_mp4)
    return resultado["text"]

# Substitua 'seu_video.mp4' pelo caminho do seu arquivo
arquivo = "video.mp4"
texto_transcrito = transcrever_video(arquivo)
print(texto_transcrito)