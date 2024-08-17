from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://0f6745fa0c913d1759.gradio.live")

if __name__ == "__main__":
  app.run()
