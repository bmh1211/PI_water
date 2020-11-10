from flask import Flask, jsonify, render_template

app=Flask(__name__)

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

if __name__=="__main__":
    app.run(debug=True)