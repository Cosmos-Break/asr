import shutil, os
from pydub import AudioSegment


if __name__ == '__main__':
    # for i in range(1, 2012 + 1):
    #     # os.rename(f'Shanghai_Dialect_Dict/Split_WAV/{i}.wav', f'Shanghai_Dialect_Dict/Split_WAV/{i-1}.wav')
    #     song = AudioSegment.from_mp3(f'Shanghai_Dialect_Dict/Split_WAV/{i}.wav')
    #     # song.set_frame_rate(16000)
    #     song.export(f'Shanghai_Dialect_Dict/Split_WAV/{i}.wav', format="wav")
    #     print(i)
    for i in range(1, 2012 + 1):
        # os.rename(f'Shanghai_Dialect_Dict/Split_WAV/{i}.wav', f'Shanghai_Dialect_Dict/Split_WAV/{i-1}.wav')
        song = AudioSegment.from_wav(f'Shanghai_Dialect_Dict/Split_WAV/{i}.wav')
        if song.duration_seconds < 0.5:
            print(123)
        # song.export(f'Shanghai_Dialect_Dict/Split_WAV/{i}.wav', format="wav")
    # cnt = 0
    # for line in open('Shanghai_Dialect_Dict/fangyan.txt', encoding='utf-8'):
    #     cnt += 1
    #     line = line.strip()
    #     open(f'Shanghai_Dialect_Dict/Split_TXT/{cnt}.txt', 'w', encoding='utf-8').write(line)
    
    # cnt = 0
    # for line in open('Shanghai_Dialect_Dict/putonghua.txt', encoding='utf-8'):
    #     cnt += 1
    #     line = line.strip()
    #     open(f'Shanghai_Dialect_Dict/Split_PROMPT/{cnt}.txt', 'w', encoding='utf-8').write(line)