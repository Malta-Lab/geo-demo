from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://51a8eeac71dfb4b081.gradio.live")

if __name__ == "__main__":
  app.run()
