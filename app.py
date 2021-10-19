from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images 
images = [
    "https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif",
    "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
    "https://media.giphy.com/media/nNxT5qXR02FOM/giphy.gif",
    "https://media.giphy.com/media/WXB88TeARFVvi/giphy.gif",
    "https://media.giphy.com/media/v6aOjy0Qo1fIA/giphy.gif",
    "https://media.giphy.com/media/Lp5wuqMOmLUaAd0jBG/giphy.gif",
    "https://media.giphy.com/media/xBAreNGk5DapO/giphy.gif",
    "https://media.giphy.com/media/9IRX12VhoXoR2/giphy.gif",
    "https://media.giphy.com/media/JoDT2WaykzFnN9vJqL/giphy.gif",
    "https://media.giphy.com/media/TKfywHrPHpJiE/giphy.gif",
    "https://media.giphy.com/media/rwCX06Y5XpbLG/giphy.gif",
    "https://media.giphy.com/media/33OrjzUFwkwEg/giphy.gif",
    "https://media.giphy.com/media/wUgWRubJHS7Ac/giphy.gif",
    "https://media.giphy.com/media/1vZ6DEZAPMH3cOtt0d/giphy.gif",
    "https://media.giphy.com/media/E0cyxhawhe9dm/giphy.gif",
    "https://media.giphy.com/media/uTCAwWNtz7U2c/giphy.gif",
    "https://media.giphy.com/media/NqZn5kPN8VVrW/giphy.gif",
    "https://media.giphy.com/media/PqdfIrXEza6fC/giphy.gif",
    "https://media.giphy.com/media/H2GT0TQBAlbuo/giphy.gif",
    "https://media.giphy.com/media/2JcGvbvNalb32/giphy.gif",
    "https://media.giphy.com/media/YJBnhs1XK9fu8/giphy.gif",
    "https://media.giphy.com/media/SJk9xTbxcg0DFDs89d/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
