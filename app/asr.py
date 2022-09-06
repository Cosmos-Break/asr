import torch
from huggingsound import SpeechRecognitionModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class ASR:
    def __init__(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = SpeechRecognitionModel("checkpoint-wav2vec2-large-xlsr-53-chinese-zh-cn-2022-09-02-10_08_26", device=device)
        self.tokenizer = self.model.processor.tokenizer
        
        mt_model_path = 'checkpoint-opus-mt-en-zh-2022-09-05-17_17_17/checkpoint-2500'
        self.mt_tokenizer = AutoTokenizer.from_pretrained(mt_model_path)
        self.mt_model = AutoModelForSeq2SeqLM.from_pretrained(mt_model_path).to(device)
        
    def transcribe(self, wav):
        audio_path = [wav]
        res = self.model.transcribe(audio_path, batch_size=1)[0]
        transcription = res['transcription']
        probabilities = res['probabilities']
        return {"transcription": transcription, "transcription_score": probabilities}

    def translation(self, text: str):
        def generate_translation(model, tokenizer, example):
            """print out the source, target and predicted raw text."""
            input_ids = example['input_ids']
            input_ids = torch.LongTensor(input_ids).view(1, -1).to(model.device)
            # print('input_ids: ', input_ids)
            generated_ids = model.generate(input_ids, max_new_tokens=64)
            # print('generated_ids: ', generated_ids)
            prediction = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
            return prediction
        
        with self.mt_tokenizer.as_target_tokenizer():
            model_inputs = self.mt_tokenizer(text, max_length=64, truncation=True)
            example = {}
            example['sh'] = text
            example['input_ids'] = model_inputs['input_ids']
            translation = generate_translation(self.mt_model, self.mt_tokenizer, example)
            
        return translation