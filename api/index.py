from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://732e48f853173d5aea.gradio.live")

if __name__ == "__main__":
  app.run()
