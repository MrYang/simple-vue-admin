from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user/logout', methods=['POST'])
def user_logout():
    return jsonify({"code": 200, "data": "success"})


@app.route('/user/login', methods=['POST'])
def user_login():
    return jsonify({"code": 200, "data": {"token": "admin-token"}})


@app.route('/user/info')
def user_info():
    return jsonify({"code": 200, "data": {
        "roles": ["admin"],
        "introduction": "I am a super administrator",
        "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
        "name": "管理员"}})


@app.route('/table/list')
def table_list():
    return jsonify({"code": 200, "data": {"total": 30,
                                          "items":
                                              [{"id": "340000199102286169",
                                                "title": "Upsov uxjcfu qbpipvyfcn utiiw uypmbrtrqr",
                                                "status": "published", "author": "name",
                                                "display_time": "1992-01-15 05:19:07",
                                                "pageviews": 394},
                                               {"id": "150000200002075647",
                                                "title": "Insur lmx fimp jobgrlqb whpiricpp",
                                                "status": "draft",
                                                "author": "name",
                                                "display_time": "1993-02-21 01:56:56",
                                                "pageviews": 2015}
                                               ]}
                    })


if __name__ == '__main__':
    app.env = 'development'
    app.run(debug=True, port=5000)
