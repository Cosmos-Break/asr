import torch
from huggingsound import SpeechRecognitionModel
import os
device = "cuda" if torch.cuda.is_available() else "cpu"
batch_size = 1
# model = SpeechRecognitionModel("wbbbbb/wav2vec2-large-chinese-zh-cn", device=device)
model = SpeechRecognitionModel("checkpoint-wav2vec2-large-xlsr-53-chinese-zh-cn-2023-08-31-09:02:50", device=device)
# audio_paths = ["Shanghai_Dialect_Dict/Split_WAV/1.wav", "Shanghai_Dialect_Dict/Split_WAV/2.wav"]
audio_paths = ["Shanghai_Dialect_Dict/Split_WAV1/1.wav"]

# audio_paths = []
# for x in os.listdir('/data/xumh/asr/zhuanrengongzhuananjian/zhuananjian'):
#     audio_paths.append('/data/xumh/asr/zhuanrengongzhuananjian/zhuananjian/' + x)
# print(audio_paths)

audio_paths = []
for x in os.listdir('/data/xumh/asr/zhuanrengongzhuananjian/zhuanrengong'):
    audio_paths.append('/data/xumh/asr/zhuanrengongzhuananjian/zhuanrengong/' + x)
print(audio_paths)



transcriptions = model.transcribe(audio_paths, batch_size=batch_size)

print(transcriptions)
