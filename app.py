from flask import Flask, request, jsonify
import item_based_rc as ibrc
import user_based_rc as ubrc
app = Flask(__name__)


@app.route("/item/<id>", methods=["GET"])
def getItemBased(id):
    return ibrc.getListItem(id)


@app.route("/user/<id>", methods=["GET"])
def getUserBased(id):
    return ubrc.getListItem(id)


if __name__ == '__main__':
    app.run(debug=True)