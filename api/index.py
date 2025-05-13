from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://2b172b9f25b19c5149.gradio.live")

if __name__ == "__main__":
  app.run()
