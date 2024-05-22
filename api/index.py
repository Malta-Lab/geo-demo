from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://7a8f248b7ebf7274ad.gradio.live")

if __name__ == "__main__":
  app.run()
