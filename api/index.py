from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://27b5200381b6e72f14.gradio.live")

if __name__ == "__main__":
  app.run()
