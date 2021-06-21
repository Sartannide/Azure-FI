from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Le port du masque est obligatoire, toute personne ne portant pas de masque se verra oblitere !'