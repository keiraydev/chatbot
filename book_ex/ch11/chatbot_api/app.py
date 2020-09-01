from flask import Flask, request, jsonify, abort
import socket
import json

# 챗봇 엔진 서버 접속 정보
host = "127.0.0.1"  # 챗봇 엔진 서버 IP 주소
port = 5050  # 챗봇 엔진 서버 통신 포트

# Flask 어플리케이션
app = Flask(__name__)


# 챗봇 엔진 서버와 통신
def get_answer_from_engine(bottype, query):
    # 챗봇 엔진 서버 연결
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # 챗봇 엔진 질의 요청
    json_data = {
        'Query': query,
        'BotType': bottype
    }
    message = json.dumps(json_data)
    mySocket.send(message.encode())

    # 챗봇 엔진 답변 출력
    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)

    # 챗봇 엔진 서버 연결 소켓 닫기
    mySocket.close()

    return ret_data


@app.route('/', methods=['GET'])
def index():
    return 'hello', 200


# 챗봇 엔진 query 전송 API
@app.route('/query/<bot_type>', methods=['POST'])
def query(bot_type):
    body = request.get_json()

    try:
        if bot_type == 'TEST':
            # 챗봇 API 테스트
            ret = get_answer_from_engine(bottype=bot_type, query=body['query'])
            return jsonify(ret)

        elif bot_type == "KAKAO":
            # 카카오톡 스킬 처리
            body = request.get_json()
            utterance = body['userRequest']['utterance']
            ret = get_answer_from_engine(bottype=bot_type, query=utterance)

            from KakaoTemplate import KakaoTemplate
            skillTemplate = KakaoTemplate()
            return skillTemplate.send_response(ret)

        elif bot_type == "NAVER":
            # 네이버톡톡 이벤트 처리
            body = request.get_json()
            user_key = body['user']
            event = body['event']

            from NaverEvent import NaverEvent
            authorization_key = '<보내기 API 인증키>'
            naverEvent = NaverEvent(authorization_key)

            if event == "open":
                # 사용자가 채팅방 들어왔을 때 처리
                print("채팅방에 유저가 들어왔습니다.")
                return json.dumps({}), 200

            elif event == "leave":
                # 사용자가 채팅방 나갔을 때 처리
                print("채팅방에 유저가 나갔습니다.")
                return json.dumps({}), 200

            elif event == "send":
                # 사용자가 챗봇에게 send 이벤트를 전송했을 때
                user_text = body['textContent']['text']
                ret = get_answer_from_engine(bottype=bot_type, query=user_text)
                return naverEvent.send_response(user_key, ret)

            return json.dumps({}), 200

        else:
            # 정의되지 않은 bot type인 경우 404 오류
            abort(404)

    except Exception as ex:
        # 오류 발생시 500 오류
        abort(500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
