from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://972981cf5f618c789c.gradio.live")

if __name__ == "__main__":
  app.run()
