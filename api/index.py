from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://b2a2307de67ad8ee63.gradio.live")

if __name__ == "__main__":
  app.run()
