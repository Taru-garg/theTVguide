from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/search', methods=['POST'])
def searchInput():
    data = request.get_json()
    print(data)
    return ''

@app.route('/search/go', methods=['POST'])
def searchEnter():
    data = request.get_json()
    print(data)
    return ''

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)