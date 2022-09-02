from datasets import load_dataset
from datasets.dataset_dict import DatasetDict
from datasets import Dataset
import os, time
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import DataCollatorForSeq2Seq, EarlyStoppingCallback
from transformers import Seq2SeqTrainingArguments, Seq2SeqTrainer
import torch

train_data = {}
sh_list = []
zh_list = []
def read_data(dataset_name):
    data_len = len(os.listdir(f'{dataset_name}/Split_TXT'))
    print(data_len)
    for cnt in range(1, data_len+1):
        sh = open(f'{dataset_name}/Split_TXT/{cnt}.txt', encoding='utf-8').readline().strip()
        zh = open(f'{dataset_name}/Split_PROMPT/{cnt}.txt', encoding='utf-8').readline().strip()
        sh_list.append(sh)
        zh_list.append(zh)
        sh_list.append(zh)
        zh_list.append(zh)

read_data('Shanghai_Dialect_Scripted_Speech_Corpus_Daily_Use_Sentence')
read_data('Shanghai_Dialect_Dict')

data = {'train':Dataset.from_dict({'sh':sh_list,'zh':zh_list})}
data = DatasetDict(data)
data = data["train"].train_test_split(test_size=0.1)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = AutoTokenizer.from_pretrained("opus-mt-en-zh")
model = AutoModelForSeq2SeqLM.from_pretrained("opus-mt-en-zh").to(device)

now = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
output_dir = f'./checkpoint-opus-mt-en-zh-{now}'

def preprocess_function(examples):
    inputs = examples['sh']
    targets = examples['zh']
    
    with tokenizer.as_target_tokenizer():
        model_inputs = tokenizer(inputs, max_length=64, truncation=True)

    with tokenizer.as_target_tokenizer():
        labels = tokenizer(targets, max_length=64, truncation=True)

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_data = data.map(preprocess_function, batched=True)

data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

batch_size = 32
# fp16=True
training_args = Seq2SeqTrainingArguments(
    output_dir=output_dir,
    evaluation_strategy="steps",
    learning_rate=2e-5,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    weight_decay=0.01,
    save_total_limit=3,
    num_train_epochs=200,
    eval_steps=100,
    load_best_model_at_end=True,
)
callbacks = [EarlyStoppingCallback(early_stopping_patience=5)]
trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_data["train"],
    eval_dataset=tokenized_data["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
    callbacks=callbacks,
)

trainer.train()

def generate_translation(model, tokenizer, example):
    """print out the source, target and predicted raw text."""
    source = example['sh']
    target = example['zh']
    input_ids = example['input_ids']
    input_ids = torch.LongTensor(input_ids).view(1, -1).to(model.device)
    print('input_ids: ', input_ids)
    generated_ids = model.generate(input_ids)
    print('generated_ids: ', generated_ids)
    prediction = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    
    print('source: ', source)
    print('target: ', target)
    print('prediction: ', prediction)

text = '侬讲呃今朝要来呃！'
text = '侬讲呃今朝要来呃！'
with tokenizer.as_target_tokenizer():
    model_inputs = tokenizer(text, max_length=64, truncation=True)
    example = {}
    example['sh'] = text
    example['zh'] = text
    example['input_ids'] = model_inputs['input_ids']
    generate_translation(model, tokenizer, example)