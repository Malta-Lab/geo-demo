from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://ffb6e73c27a2f35424.gradio.live")

if __name__ == "__main__":
  app.run()
