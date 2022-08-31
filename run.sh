# for i in wav2vec2-large-chinese-zh-cn wav2vec2-large-xlsr-53-chinese-zh-cn wav2vec2-large-xlsr-53-chinese-zh-cn-gpt wav2vec2-large-xlsr-53-chinese-zn-cn-aishell1;
for i in wav2vec2-large-xlsr-53-chinese-zh-cn-gpt wav2vec2-large-xlsr-53-chinese-zn-cn-aishell1;
# for i in wav2vec2-large-chinese-zh-cn wav2vec2-large-xlsr-53-chinese-zh-cn-gpt wav2vec2-large-xlsr-53-chinese-zn-cn-aishell1;
do
    echo $i is appoint;
    date=$(date "+%Y%m%d-%H%M%S")
    python3 train.py $i | tee log_${i}_${date}
done