import shutil
from pydub import AudioSegment
cnt = 0

def split(PROMPT, TRANSCRIPTION, wav_file):
    global cnt
    cnt += 1
    output_dir = 'Shanghai_Dialect_Scripted_Speech_Corpus_Daily_Use_Sentence'
    open(f'{output_dir}/Split_TXT/{cnt}.txt', 'w', encoding='utf-8').write(TRANSCRIPTION)
    open(f'{output_dir}/Split_PROMPT/{cnt}.txt', 'w', encoding='utf-8').write(PROMPT)
    wav = AudioSegment.from_wav(wav_file) # 打开wav文件
    if wav.duration_seconds < 2:
        print(123)
    shutil.copyfile(wav_file, f'{output_dir}/Split_WAV/{cnt}.wav')
    
if __name__ == '__main__':
    f = open('Shanghai_Dialect_Scripted_Speech_Corpus_Daily_Use_Sentence/UTTRANSINFO.txt', encoding='utf-8')
    f.readline()
    for line in f:
        line = line.strip()
        CHANNEL, UTTRANS_ID, SPEAKER_ID, PROMPT, TRANSCRIPTION = line.split('\t')
        wav_file = f'Shanghai_Dialect_Scripted_Speech_Corpus_Daily_Use_Sentence/WAV/{SPEAKER_ID}/{UTTRANS_ID}'
        split(PROMPT, TRANSCRIPTION, wav_file)