from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://6e8e6c9e3ba04857a3.gradio.live")

if __name__ == "__main__":
  app.run()
