from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://4d58b6b6fc02ec6bec.gradio.live")

if __name__ == "__main__":
  app.run()
