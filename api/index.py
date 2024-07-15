from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://50631f10db8fcb8cfd.gradio.live")

if __name__ == "__main__":
  app.run()
