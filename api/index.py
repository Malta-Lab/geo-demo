from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://d6bdd1d0f60660bd52.gradio.live")

if __name__ == "__main__":
  app.run()
