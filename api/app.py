from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://931d3aa56075f393cf.gradio.live")

if __name__ == "__main__":
  app.run()
