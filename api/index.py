from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://f8ece9ab2d10c6d0c1.gradio.live")

if __name__ == "__main__":
  app.run()
