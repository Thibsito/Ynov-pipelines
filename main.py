from bottle import route, run, template
from misc import add


@route("/hello/<name>")
def index(name):
    return template("<b>Hello {{name}}</b>!", name=name)


@route("/")
def homepage():
    return "<b>Hello you</b>!"


@route("/add/<a>/<b>")
@route("/add/<a>/<b>/")
def route_add(a, b):
    return {"result": add(a, b)}


if __name__ == "__main__":
    run(host="localhost", port=8080, reloader=True)
