import requests, json

# 보내기 API 인증키
authorization_key = '<보내기 API 인증키>'
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Authorization': authorization_key,
}

# 사용자 식별값, 보낼 메시지 정의
user_key = '<메시지 전송 대상 사용자 식별값>'
data = {
    "event": "send",
    "user": user_key,
    "textContent": {"text": "hello world :D"}
}

# 보내기 API 호출
message = json.dumps(data) # JSON 문자열 변경
response = requests.post(
    'https://gw.talk.naver.com/chatbot/v1/event',
    headers=headers,
    data=message)
print(response.status_code)
print(response.text)
