from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://d678e45653bc29cf16.gradio.live")

if __name__ == "__main__":
  app.run()
