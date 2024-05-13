# from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor, TrainingArguments, Trainer
# import os


# model = Wav2Vec2ForCTC.from_pretrained("wav2vec2-large-xlsr-53-chinese-zh-cn")
# processor = Wav2Vec2Processor.from_pretrained("wav2vec2-large-xlsr-53-chinese-zh-cn")
# from transformers import Wav2Vec2CTCTokenizer

# new_vocab_file = "new_vocab.json"
# new_tokenizer = Wav2Vec2CTCTokenizer(
#     new_vocab_file, 
#     unk_token="[UNK]", 
#     pad_token="[PAD]", 
#     word_delimiter_token="|"
# )
# # from transformers.models.wav2vec2.modeling_wav2vec2 import Wav2Vec2ForCTC

# config = model.config
# config.vocab_size = len(new_tokenizer)

# new_model = Wav2Vec2ForCTC(config)
# new_model.wav2vec2.load_state_dict(model.wav2vec2.state_dict())
# new_model.lm_head = model.lm_head
# new_model.lm_head.weight = model.lm_head.weight.new_zeros(config.vocab_size, config.hidden_size)
# new_model.lm_head.bias = model.lm_head.bias.new_zeros(config.vocab_size)

# new_processor = Wav2Vec2Processor(
#     feature_extractor=processor.feature_extractor,
#     tokenizer=new_tokenizer
# )

# # 使用新的processor和model进行训练和推理
# output_dir = "wav2vec2-large-xlsr-53-chinese-zh-cn-new"

# # 保存模型
# model.save_pretrained(output_dir)

# # 如果您还想要保存训练的配置
# training_args = TrainingArguments(output_dir=output_dir, ...)  # 根据实际情况初始化TrainingArguments
# training_args.to_json_file(os.path.join(output_dir, 'training_args.json'))

# # 保存词汇表
# new_tokenizer.save_pretrained(output_dir)