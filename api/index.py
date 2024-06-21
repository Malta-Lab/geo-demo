from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://95c7c8562c0969027c.gradio.live")

if __name__ == "__main__":
  app.run()
