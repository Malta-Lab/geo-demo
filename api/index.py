from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://8601784ba8cfa5e21e.gradio.live")

if __name__ == "__main__":
  app.run()
