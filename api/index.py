from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://622ce7346c6f7ee55a.gradio.live")

if __name__ == "__main__":
  app.run()
