from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://fe1d5ae49d544c2036.gradio.live")

if __name__ == "__main__":
  app.run()
