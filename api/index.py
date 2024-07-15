from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://354a6b21f34e137e28.gradio.live")

if __name__ == "__main__":
  app.run()
