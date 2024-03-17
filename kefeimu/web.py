# app.py (使用Flask框架)
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_message = data['message']

    # 调用OpenAI API
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_message,
        max_tokens=50
    )

    # 从响应中获取文本回复
    reply = response.choices[0].text.strip()

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)

