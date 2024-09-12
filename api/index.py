from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://16e689e75c73015056.gradio.live")

if __name__ == "__main__":
  app.run()
