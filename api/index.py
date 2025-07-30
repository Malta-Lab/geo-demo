from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://c90375b3a31a8f9980.gradio.live")

if __name__ == "__main__":
  app.run()
