from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://59b4cd8fc67661c1b2.gradio.live")

if __name__ == "__main__":
  app.run()
