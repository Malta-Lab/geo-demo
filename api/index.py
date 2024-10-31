from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://fe3a0078b4268c2313.gradio.live")

if __name__ == "__main__":
  app.run()
