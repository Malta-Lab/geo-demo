from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://4c12195e4d1650be71.gradio.live")

if __name__ == "__main__":
  app.run()
