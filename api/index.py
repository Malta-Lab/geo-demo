from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://04c080eb71e3ff764a.gradio.live")

if __name__ == "__main__":
  app.run()
