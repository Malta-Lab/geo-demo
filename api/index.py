from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://a1c00f64e05004a6b4.gradio.live")

if __name__ == "__main__":
  app.run()
