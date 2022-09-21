## 使用的工具库
Huggingface的transformers和huggingsound。

## 沪语ASR模型

包含一个沪语ASR模型(沪语语音->沪语转写文本)和机器翻译模型(沪语转写文本->普通话文本)。

## 数据
包含Magichub开源数据集、喜马拉雅，中国语言网爬取的数据集、讯飞TTS生成的wav数据。

## 训练脚本
train.py 用于训练ASR模型
train_translation.py 用于训练MT模型

## 服务
使用fastapi进行整个模型的部署，运行run_service.sh部署。

