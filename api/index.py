from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://5d1ec5f749805b1a57.gradio.live")

if __name__ == "__main__":
  app.run()
