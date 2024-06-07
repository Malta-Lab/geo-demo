from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://26c507e77b621f8202.gradio.live")

if __name__ == "__main__":
  app.run()
