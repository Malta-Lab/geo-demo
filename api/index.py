from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://765417840a54d11594.gradio.live")

if __name__ == "__main__":
  app.run()
