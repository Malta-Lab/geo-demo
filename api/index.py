from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://eb119b0188edd85e46.gradio.live")

if __name__ == "__main__":
  app.run()
