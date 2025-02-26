from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://2bcb5e52889a03460f.gradio.live")

if __name__ == "__main__":
  app.run()
