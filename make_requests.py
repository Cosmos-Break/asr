import requests
import json

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5,ja;q=0.4,my;q=0.3',
    'Connection': 'keep-alive',
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
    'Origin': 'http://127.0.0.1:8000',
    'Referer': 'http://127.0.0.1:8000/docs',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
    'accept': 'application/json',
    'sec-ch-ua': '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'input': 'Shanghai_Dialect_Conversational_Speech_Corpus/Split_WAV2/1.wav',
    'output': 'string',
}

response = requests.post('http://127.0.0.1:8000/transcribe/', headers=headers, json=json_data)
# print(response.json())
print(json.dumps(response.json(), indent=4, ensure_ascii=False))