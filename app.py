from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/')
def main():
    cmd = request.args.get('cmd', default='alert(1)', type=str)

    return Response(cmd, mimetype='application/javascript')

if __name__ == '__main__':
    app.run('0.0.0.0')