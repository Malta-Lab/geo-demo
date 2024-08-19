from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://ec212d3221e283f8ae.gradio.live")

if __name__ == "__main__":
  app.run()
