from flask import Flask,request
import json   
from flask_cors import CORS
from langchain_mail import create_mail

app = Flask(__name__)
CORS(app)
app.json.ensure_ascii = False   # 文字化けを防ぐ

# POSTに対する処理
@app.route('/', methods=['POST'])
def mail():     
    try:
        content = request.json["content"]
        modified_content, subject = create_mail(content)
        # modified_content, subject = "これが修正された内容です", "これが件名です"

        response = {
            "status": "success",
            "detail": {
                "modified_content": modified_content,
                "subject": subject    
            }
        }
    except Exception as e:
        response = {
            "status": "fail",
            "detail": str(e)
            }
    return json.dumps(response, ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)