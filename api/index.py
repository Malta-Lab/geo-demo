from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://89d7c460372aa6ae03.gradio.live")

if __name__ == "__main__":
  app.run()
