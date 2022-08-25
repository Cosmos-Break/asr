from huggingsound import TrainingArguments, ModelArguments, SpeechRecognitionModel, TokenSet
import os, random
model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-chinese-zh-cn")
output_dir = "output"

# first of all, you need to define your model's token set
# however, the token set is only needed for non-finetuned models
# if you pass a new token set for an already finetuned model, it'll be ignored during training
# tokens = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "'"]
# token_set = TokenSet(tokens)

# define your train/eval data
train_data = []

def read_data(dataset_name):
    data_len = len(os.listdir(f'{dataset_name}/Split_TXT'))
    print(data_len)
    for cnt in range(1, data_len+1):
        transcription = open(f'{dataset_name}/Split_TXT/{cnt}.txt', encoding='utf-8').readline().strip()
        path = f'{dataset_name}/Split_WAV/{cnt}.wav'
        train_data.append(
            {"path": path, "transcription":transcription}
        )
read_data('Shanghai_Dialect_Conversational_Speech_Corpus')
read_data('Shanghai_Dialect_Scripted_Speech_Corpus_Daily_Use_Sentence')
random.shuffle(train_data)
eval_ratio = 0.2
index = int(len(train_data) * eval_ratio)
eval_data = train_data[:index]
train_data = train_data[index:]
print('eval_data_len:', len(eval_data))
print('train_data_len:', len(train_data))

# fp16=True,
batch_size = 16
training_args = TrainingArguments(
    group_by_length=True,
    num_train_epochs=200,
    learning_rate=1e-4,
    eval_steps=100,
    warmup_steps=10,
    gradient_checkpointing=True,
    weight_decay=0.005,
    save_total_limit=2,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    gradient_accumulation_steps=2,
    early_stopping_patience=5,
)
model_args = ModelArguments(
    activation_dropout=0.1,
    hidden_dropout=0.1,
) 

model.finetune(
    output_dir, 
    train_data=train_data, 
    eval_data=eval_data, # the eval_data is optional
    training_args=training_args,
    model_args=model_args,
)
