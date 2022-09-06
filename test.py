import requests
import json

cookies = {
    'JSESSIONID': 'fOEQkywi7y7Slldhvj97xAalA9TrxvXubTUtiCa7Eh88VODDg7gE!1526488717',
    'ROUTEID': '.server2',
}

headers = {
    'Host': 'workingenv1.bosc.cn:3601',
    'x-mgs-encryption': '1',
    'AppId': '65854C1021501',
    'WorkspaceId': 'product',
    'productId': '65854C1021501_IOS',
    'Accept': '*/*',
    'productVersion': '10.1.68.27cp0312110000',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Operation-Type': 'iom.wa.com.bos.wa.manger.mobile.insertWorkData.biz.ext',
    'Platform': 'IOS',
    'UniformGateway': 'https://workingenv1.bosc.cn:3601/mgw.htm',
    'User-Agent': 'ShangHangEWork/1 CFNetwork/1335.0.3 Darwin/21.6.0',
    'Connection': 'keep-alive',
    'Ts': 'OCGcKcE',
    'Content-Type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'JSESSIONID=fOEQkywi7y7Slldhvj97xAalA9TrxvXubTUtiCa7Eh88VODDg7gE!1526488717; ROUTEID=.server2',
    'Sign': '363f012cf6542aa114d41dd5987444ed',
}

data = 'AwAAIQPCbjsx0BDn/AXJcuPGJs/lxzUYkxV7YMCOGUp92SUXVg0AAWAGZAt/25FqfRBoOChlgiFT4CiLHWcBU0QHpH5Wtg9eXBwaT1UFp4UM9HrcZwUsqNqhZS2Biyx9sWevBOyX288nnmDyvhQxSQT2dKE/BZ2VaXVahwASVmNKQpOCUnE86xE6SgDVA1Lygkm/fBcyO+CUutQEngs1sV+SgdQ9URQ9Xyy7Wv7XN2qfGlvEJzCY/a3NPOpy7pfo8o0Cu2nrP5o3XZVqBAaA7pOX0pOdON7pS7KAae9S00ZePSjWaNR6rfHqqRNub0w+BgJjsECASlpyBKA6r0gCEjBo6Rolg6B02t0h1Q2llZm4N6Mbvr8R+0fcriF2sCxTN/MRdwyTZEfDFnWy66AudbqxPDDSqa9Qd11lV7FDWPMWgi3ywFZwNcPTHZLdJBC3CpHitO1ictURgmVGEr8KrvhnVfvjQt3RLDKmb4xO8zYnZJnkcuxsdTNeoOPcNU4nVXoD5uuY2TFn'

response = requests.post('https://workingenv1.bosc.cn:3601/mgw.htm', cookies=cookies,data=json.dumps(data), headers=headers, verify=False)

with open('0.dat', 'wb') as f:
    f.write(response.content)