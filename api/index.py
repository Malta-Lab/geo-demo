from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://c18d10b578a0e667a3.gradio.live")

if __name__ == "__main__":
  app.run()
