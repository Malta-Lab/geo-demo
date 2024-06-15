from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://954dbd071c8537e49e.gradio.live")

if __name__ == "__main__":
  app.run()
