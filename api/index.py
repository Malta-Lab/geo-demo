from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://a35f3163a80f92f3ce.gradio.live")

if __name__ == "__main__":
  app.run()
