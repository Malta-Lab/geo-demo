from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://97b0ff9f79fec378a4.gradio.live")

if __name__ == "__main__":
  app.run()
