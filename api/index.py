from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://07fd842c2672576c9d.gradio.live")

if __name__ == "__main__":
  app.run()
