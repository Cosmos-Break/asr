import shutil, os
from pydub import AudioSegment


if __name__ == '__main__':
    cnt = 0
    for line in open('Shanghai_Dialect_Ximalaya/fangyan.txt', encoding='utf-8'):
        cnt += 1
        line = line.strip()
        open(f'Shanghai_Dialect_Ximalaya/Split_TXT/{cnt}.txt', 'w', encoding='utf-8').write(line)
    
    cnt = 0
    for line in open('Shanghai_Dialect_Ximalaya/putonghua.txt', encoding='utf-8'):
        cnt += 1
        line = line.strip()
        open(f'Shanghai_Dialect_Ximalaya/Split_PROMPT/{cnt}.txt', 'w', encoding='utf-8').write(line)