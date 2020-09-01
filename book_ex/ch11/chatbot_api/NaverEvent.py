import requests, json

class NaverEvent:
    def __init__(self, authorization):
        self.authorization_key = authorization

    # 텍스트 컨텐트 출력 요소
    def textContentComponent(self, text):
        return {
            "textContent": {
                "text": text
            }
        }

    # 이미지 컨텐트 출력 요소
    def imageContentComponent(self, imageUrl):
        return {
            "imageContent": {
                "imageUrl": imageUrl
            }
        }

    # 보내기 API로 메시지 전송
    def send_message(self, user_key, component):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': self.authorization_key,
        }

        data = {
            "event": "send",
            "user": user_key,
        }
        data.update(component)

        # 보내기 API 호출
        message = json.dumps(data)  # JSON 문자열 변경
        return requests.post(
            'https://gw.talk.naver.com/chatbot/v1/event',
            headers=headers,
            data=message)

    # 사용자에게 응답 전송
    def send_response(self, dst_user_key, bot_resp):
        # 이미지 답변이 텍스트 답변보다 먼저 출력 됨
        # 이미지 답변이 있는 경우
        if bot_resp['AnswerImageUrl'] is not None:
            image = self.imageContentComponent(bot_resp['AnswerImageUrl'])
            self.send_message(user_key=dst_user_key, component=image)

        # 텍스트 답변이 있는 경우
        if bot_resp['Answer'] is not None:
            text = self.textContentComponent(bot_resp['Answer'])
            self.send_message(user_key=dst_user_key, component=text)

        return json.dumps({}), 200
