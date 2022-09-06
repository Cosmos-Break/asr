from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.asr import ASR

class Message(BaseModel):
    input: str
    output: str = None

app = FastAPI()
asr = ASR()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/transcribe/")
async def  transcribe(message: Message):
    # wav = "Shanghai_Dialect_Dict/Split_WAV/1.wav"
    wav = message.input
    transcribe_json_data  = asr.transcribe(wav=wav)
    transcription = transcribe_json_data['transcription']
    translation = asr.translation(text=transcription)
    transcribe_json_data['possible_translation'] = translation
    # message.output = json.dumps(transcribe_json_data)
    message.output = transcribe_json_data
    return {"output" : message.output}

# @app.post("/sentiment/")
# async def sentiment_analysis(message: Message):
#     message.output  = str(asr.sentiments(message.input))
#     return {"output" : message.output}