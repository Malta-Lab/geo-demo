from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://233c71d616dde9712d.gradio.live")

if __name__ == "__main__":
  app.run()
