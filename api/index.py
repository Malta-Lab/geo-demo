from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://bbd2e76485d72580fc.gradio.live")

if __name__ == "__main__":
  app.run()
