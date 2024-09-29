from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://206b3571529c420e84.gradio.live")

if __name__ == "__main__":
  app.run()
