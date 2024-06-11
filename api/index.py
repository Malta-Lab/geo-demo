from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://3924fce783b0155873.gradio.live")

if __name__ == "__main__":
  app.run()
