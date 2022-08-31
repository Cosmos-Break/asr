import shutil, os
from pydub import AudioSegment


if __name__ == '__main__':
    # for i in range(2, 2013 + 1):
    #     os.rename(f'Shanghai_Dialect_Dict/wav/{i}.wav', f'Shanghai_Dialect_Dict/wav/{i-1}.wav')
    cnt = 0
    for line in open('Shanghai_Dialect_Dict/fangyan.txt', encoding='utf-8'):
        cnt += 1
        line = line.strip()
        open(f'Shanghai_Dialect_Dict/Split_TXT/{cnt}.txt', 'w', encoding='utf-8').write(line)
    
    cnt = 0
    for line in open('Shanghai_Dialect_Dict/putonghua.txt', encoding='utf-8'):
        cnt += 1
        line = line.strip()
        open(f'Shanghai_Dialect_Dict/Split_PROMPT/{cnt}.txt', 'w', encoding='utf-8').write(line)