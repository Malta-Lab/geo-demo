from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://9f013b37a658c49184.gradio.live")

if __name__ == "__main__":
  app.run()
