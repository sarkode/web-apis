from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def python():
        return render_template('python.html')

@app.route('/whereami')
def whereami():
        return "Kdua"

if __name__ == '__main__':
        app.run(host="0.0.0.0")
