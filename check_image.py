import json

transcript_path = 'C:/Users/gomus/.gemini/antigravity-ide/brain/ac6d1c9e-739c-4812-9f93-2fd35a873be5/.system_generated/logs/transcript_full.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'USER_INPUT':
            content = str(data.get('content', ''))
            if 'fotke mojego studia' in content:
                print("Keys:", data.keys())
                for k, v in data.items():
                    if k != 'content':
                        print(k, ":", str(v)[:300])
                    else:
                        print(k, ":", str(v))
