from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://299a238dff8cd313eb.gradio.live")

if __name__ == "__main__":
  app.run()
