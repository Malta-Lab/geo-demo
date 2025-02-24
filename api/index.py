from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://d9779ac1d7e962b497.gradio.live")

if __name__ == "__main__":
  app.run()
