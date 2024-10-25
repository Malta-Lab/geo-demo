from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://2ee366733f3a1b965e.gradio.live")

if __name__ == "__main__":
  app.run()
