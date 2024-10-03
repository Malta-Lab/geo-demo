from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://ab8e2a49eec732128a.gradio.live")

if __name__ == "__main__":
  app.run()
