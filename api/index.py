from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://0c9478662577028f89.gradio.live")

if __name__ == "__main__":
  app.run()
