from flask import Flask, request, jsonify
app = Flask(__name__)

# 서버 리소스
resource = []

# 사용자 정보 조회
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):

    for user in resource:
        if user['user_id'] is user_id:
            return jsonify(user)

    return jsonify(None)


# 사용자 추가
@app.route('/user', methods=['POST'])
def add_user():
    user = request.get_json()
    resource.append(user)
    return jsonify(resource)



if __name__ == '__main__':
    app.run()
