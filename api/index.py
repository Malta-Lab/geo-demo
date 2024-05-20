from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://0a426509900bf56fcc.gradio.live")

if __name__ == "__main__":
  app.run()
