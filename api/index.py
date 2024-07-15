from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://98b66e4ee00ef5ceeb.gradio.live")

if __name__ == "__main__":
  app.run()
