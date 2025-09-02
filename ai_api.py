import requests
import json

def main():
    url = "https://qianfan.baidubce.com/v2/chat/completions"
    
    payload = json.dumps({
        "model": "ernie-lite-8k",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": input("请输入问题:")
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer bce-v3/ALTAK-Fzr5eyTwE3RJNpj4Nrpus/0a1635406010b6eb403e7a3c1e87cb985ff33a72'
    }
    
    resp= requests.request("POST", url, headers=headers, data=payload)
    
    print(resp.json()['choices'][0]['message']['content'])
    

if __name__ == '__main__':
    while(1):
        main()