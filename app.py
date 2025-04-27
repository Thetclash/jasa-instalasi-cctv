from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    from os import getenv
    port = int(getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)