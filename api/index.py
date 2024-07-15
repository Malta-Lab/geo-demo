from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://90da9df85bfe47937d.gradio.live")

if __name__ == "__main__":
  app.run()
