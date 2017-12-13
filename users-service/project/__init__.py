from flask import Flask, jsonify


def create_app(app_settings=[]):
    app = Flask(__name__)
    app.config.from_object(app_settings)
    return app


app = create_app()


@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
