import flask

app = flask.Flask(__name__)

@app.route('/backend',methods=['GET']) # 瀏覽網頁路徑 /backend 時要做甚麼
def test():
    ans = int(request.args['a']) + int(request.args['b'])  # 參數 a 加上 參數 b，將結果存入 ans
    with open('/tmp/nowtest.txt', 'w') as f:
        f.write(str(ans))  # 將 ans 內容輸出到 /tmp/nowtest.txt 檔案內
    return str(ans) # 回傳 ans 內容

if __name__ == "__main__":
    app.run()