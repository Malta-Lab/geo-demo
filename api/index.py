from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://e3c4e7bfa57bf50e26.gradio.live")

if __name__ == "__main__":
  app.run()
