from flask import Flask, jsonify, render_template
from flask_cors import CORS,cross_origin

app=Flask(__name__)
app.config.from_object(__name__)
CORS(app, support_credentials=True)
g_btn_status = "None"

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/server_info')
def info():
    data={'server_name' : '0,0,0,0','server_port':'8080'}
    return jsonify(data)

@app.route('/view')
def ex():
    return render_template('view.html')

@app.route('/view_easy')
def ex2():
    return render_template('view_easy.html')


#author: hyeok0724.kim@ninewatt.com
#param: None
#description: Get btn_value
@app.route('/polling')
def polling():
    global g_btn_status
    print("========== %s" %g_btn_status)
    return jsonify({"polling" : g_btn_status}), 200


#author: hyeok0724.kim@ninewatt.com
#param: status
#ex) on or off
#description: Get status
@app.route('/btn_status/<status>')
def btn_status(status):

    print(status)
    global g_btn_status
    g_btn_status = status

    return jsonify({"btn_status" :g_btn_status}), 200

if __name__ == "__main__":
    app.host = "127.0.0.1"
    app.port = "5000"
    app.debug = True
    app.run()