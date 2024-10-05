from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://f3300623861c272278.gradio.live")

if __name__ == "__main__":
  app.run()
