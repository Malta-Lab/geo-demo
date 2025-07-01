from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://05f2e73c9272610a7b.gradio.live")

if __name__ == "__main__":
  app.run()
