from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://c4d7ef5a44a0b56710.gradio.live")

if __name__ == "__main__":
  app.run()
