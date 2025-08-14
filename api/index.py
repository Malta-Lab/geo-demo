from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://faefb563f7b53eb9e8.gradio.live")

if __name__ == "__main__":
  app.run()
