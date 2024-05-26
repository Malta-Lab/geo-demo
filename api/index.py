from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://8c1f9fcb3719c2656e.gradio.live")

if __name__ == "__main__":
  app.run()
