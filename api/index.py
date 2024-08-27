from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://2da3e6c0d3c2f5fa93.gradio.live")

if __name__ == "__main__":
  app.run()
