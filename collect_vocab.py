from huggingsound import TrainingArguments, ModelArguments, SpeechRecognitionModel, TokenSet
import os, random, time
import torch
import numpy as np
import sys
import json

def isChinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

def read_data(dataset_name):
    data_len = len(os.listdir(f'{dataset_name}/Split_TXT'))
    print(data_len)
    for cnt in range(1, data_len+1):
        transcription = open(f'{dataset_name}/Split_TXT/{cnt}.txt', encoding='utf-8').readline().strip()
        for char in transcription:
            if char not in char_dict:
                char_dict[char] = 0
            char_dict[char] += 1

if __name__ == '__main__':
    vocab = json.load(open('wav2vec2-large-xlsr-53-chinese-zh-cn/vocab.json', encoding='utf-8'))
    start_cnt = len(vocab)
    char_dict = {}
    read_data('Shanghai_Dialect_Conversational_Speech_Corpus')
    read_data('Shanghai_Dialect_Scripted_Speech_Corpus_Daily_Use_Sentence')
    read_data('Shanghai_Dialect_Dict')
    read_data('Shanghai_Dialect_Zhongguoyuyan')
    for char in char_dict:
        if char not in vocab and char_dict[char] > 10 and isChinese(char):
            print(char, char_dict[char])
            vocab[char] = start_cnt
            start_cnt += 1