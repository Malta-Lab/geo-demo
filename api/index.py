from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://b7026bbe4f71d4c2fd.gradio.live")

if __name__ == "__main__":
  app.run()
