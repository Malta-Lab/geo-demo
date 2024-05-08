from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://4db77d291a326f543e.gradio.live")

if __name__ == "__main__":
  app.run()
