# fastest_api_mocker

基于 Flask的快速 API Mocker!

# 安装

```
virtualenv --no-site-packages venv
. ./venv/bin/activate
pip3 install -r requirements.txt
```

# 配置

按需修改：

```
 app.run(host = "127.0.0.1",port = 6660,debug = True)
```

中的地址与端口
 
# 运行

```
python3 mocker.py
```

# 写接口

参考`mocker.py`中的这个例子！

```
@app.route("/handle_data", methods=['POST'])
def handle_data():
    body = trans(request.get_data())
    if not body.get("method") in ["base16","base32","base58","base64"]:
        return error
    if body.get("payload") == None:
        return error
    return success
```
