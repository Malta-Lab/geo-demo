from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://fc63025ae8d883eda0.gradio.live")

if __name__ == "__main__":
  app.run()
