from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://5fdcaa1c4f22af5712.gradio.live")

if __name__ == "__main__":
  app.run()
