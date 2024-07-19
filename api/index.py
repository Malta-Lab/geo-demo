from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://d443afc48f63caaf57.gradio.live")

if __name__ == "__main__":
  app.run()
