from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://03fd12b4ca9d0bc3ef.gradio.live")

if __name__ == "__main__":
  app.run()
