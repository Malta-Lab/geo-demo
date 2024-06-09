from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://e185ef9a7d7c098d61.gradio.live")

if __name__ == "__main__":
  app.run()
