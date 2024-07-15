from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://0507f8945be30862ec.gradio.live")

if __name__ == "__main__":
  app.run()
