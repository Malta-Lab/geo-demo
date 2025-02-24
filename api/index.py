from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://39ddbb82a0102c7671.gradio.live")

if __name__ == "__main__":
  app.run()
