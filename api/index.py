from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://3fb92df24c51d22662.gradio.live")

if __name__ == "__main__":
  app.run()
