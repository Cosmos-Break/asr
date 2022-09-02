import torch
from huggingsound import SpeechRecognitionModel

device = "cuda" if torch.cuda.is_available() else "cpu"
batch_size = 1
# model = SpeechRecognitionModel("wbbbbb/wav2vec2-large-chinese-zh-cn", device=device)
model = SpeechRecognitionModel("checkpoint-wav2vec2-large-xlsr-53-chinese-zh-cn-2022-09-02-10_08_26", device=device)
# audio_paths = ["Shanghai_Dialect_Dict/Split_WAV/1.wav", "Shanghai_Dialect_Dict/Split_WAV/2.wav"]
audio_paths = ["Shanghai_Dialect_Dict/Split_WAV/1.wav"]

transcriptions = model.transcribe(audio_paths, batch_size=batch_size)

print(transcriptions)
