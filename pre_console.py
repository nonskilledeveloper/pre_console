from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/<enterprise_name>")
def hello_world(enterprise_name):

    return render_template('pre_console.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")