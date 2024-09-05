from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://8a4b9ee9b64835f515.gradio.live")

if __name__ == "__main__":
  app.run()
