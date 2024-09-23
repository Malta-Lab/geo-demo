from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://0bb701e61272e90a5d.gradio.live")

if __name__ == "__main__":
  app.run()
