from flask import Flask, request, render_template

app = Flask(__name__)


def mean(seq: str):
    L = []
    for number in seq.split(";"):
        L.append(int(number))
        mean = statistics.mean(L)
    return mean


@app.route('/')
def hello():
    return render_template('get_numbers.html')


@app.route('/seq', methods = ['GET'])
def get_seq():
    seq = request.arg("seq")
    return mean(seq)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
