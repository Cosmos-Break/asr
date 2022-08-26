import os
from pydub import AudioSegment

cnt = 0
bad_cnt = 0

def split(txt_file, wav_file):
    global cnt
    global bad_cnt
    output_dir = 'Shanghai_Dialect_Conversational_Speech_Corpus'
    wav = AudioSegment.from_wav(wav_file) # 打开wav文件
    # wav[17*1000+500:].export(f'{output_dir}/Split_TXT/{cnt}.wav', format="wav") # 切割前17.5秒并覆盖保存
    
    for line in open(txt_file, encoding='utf-8'):
        line = line.strip().split('\t')
        timestamp = line[0]
        ltime, rtime = timestamp[1:-1].split(',')
        ltime = int(float(ltime) * 1000)
        rtime = int(float(rtime) * 1000)
        # print(rtime - ltime)
        if rtime - ltime < 1000:
            bad_cnt += 1
            continue
        speaker = line[1]
        gender = line[2]
        transcription = line[3]
        if '[' in transcription:
            continue
        if len(transcription) < 5:
            print(transcription)
        cnt += 1
        wav[ltime:rtime].export(f'{output_dir}/Split_WAV/{cnt}.wav', format="wav")
        open(f'{output_dir}/Split_TXT/{cnt}.txt', 'w', encoding='utf-8').write(transcription)
        

if __name__ == '__main__':
    files = os.listdir('Shanghai_Dialect_Conversational_Speech_Corpus/TXT')
    for file in files:
        file = file.split('.')[0]
        txt_file = f'Shanghai_Dialect_Conversational_Speech_Corpus/TXT/{file}.txt'
        wav_file = f'Shanghai_Dialect_Conversational_Speech_Corpus/WAV/{file}.wav'
        split(txt_file, wav_file)