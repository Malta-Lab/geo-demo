from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://3a46957f16b7ac60f1.gradio.live")

if __name__ == "__main__":
  app.run()
