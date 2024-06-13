from flask import Blueprint,render_template
from apps.app import db
from apps.talk.models import talk
talk = Blueprint(
    "talk",
    __name__,
    template_folder="templates",
    static_folder="static",
)
@talk.route("/")
def index():
    return render_template("talk/index.html")
@talk.route("/sql")
def sql():
    db.session.query(talk).all()

@talk.route("/friends")
def friends():
    return render_template("talk/friends.html")

@talk.route("/chats")
def chats():
    return render_template("talk/chats.html")
@talk.route("/chat")
def chat():
    return render_template("talk/chat.html")