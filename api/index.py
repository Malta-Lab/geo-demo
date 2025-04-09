from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://0ca305f560d40f6fbe.gradio.live")

if __name__ == "__main__":
  app.run()
