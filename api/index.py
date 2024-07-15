from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://0b1face362dc5268bb.gradio.live")

if __name__ == "__main__":
  app.run()
