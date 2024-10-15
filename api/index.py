from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://879c2a751e8d977591.gradio.live")

if __name__ == "__main__":
  app.run()
