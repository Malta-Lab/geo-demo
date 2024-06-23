from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://7d63d7227b4fd6254f.gradio.live")

if __name__ == "__main__":
  app.run()
