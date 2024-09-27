from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://90b45594f09b980dec.gradio.live")

if __name__ == "__main__":
  app.run()
