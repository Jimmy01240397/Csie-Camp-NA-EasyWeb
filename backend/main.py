import flask
import os

app = flask.Flask(__name__)

@app.route('/backend/write',methods=['GET']) # 瀏覽網頁路徑 /backend/write 時要做甚麼
def write():
    ans = int(flask.request.args['a']) + int(flask.request.args['b'])  # 參數 a 加上 參數 b，將結果存入 ans
    with open('/tmp/nowtest.txt', 'w') as f:
        f.write(str(ans))  # 將 ans 內容輸出到 /tmp/nowtest.txt 檔案內
    return str(ans) # 回傳 ans 內容

@app.route('/backend/read',methods=['GET']) # 瀏覽網頁路徑 /backend/read 時要做甚麼
def read():
    if not os.path.exists('/tmp/nowtest.txt'): # 如果 /tmp/nowtest.txt 檔案不存在，回傳 "Not Found"，並結束該函式
        return "Not Found"
    with open('/tmp/nowtest.txt', 'r') as f:
        return f.read()  # 回傳 /tmp/nowtest.txt 檔案的內容

if __name__ == "__main__":
    app.run()
