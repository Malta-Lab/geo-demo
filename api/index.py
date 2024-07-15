from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://a1c4fa497bc5bf809e.gradio.live")

if __name__ == "__main__":
  app.run()
