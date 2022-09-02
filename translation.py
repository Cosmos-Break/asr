from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = AutoTokenizer.from_pretrained("opus-mt-en-zh")
model = AutoModelForSeq2SeqLM.from_pretrained("opus-mt-en-zh").to(device)

def generate_translation(model, tokenizer, example):
    """print out the source, target and predicted raw text."""
    source = example['sh']
    target = example['zh']
    input_ids = example['input_ids']
    input_ids = torch.LongTensor(input_ids).view(1, -1).to(model.device)
    # print('input_ids: ', input_ids)
    generated_ids = model.generate(input_ids, max_new_tokens=64)
    # print('generated_ids: ', generated_ids)
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