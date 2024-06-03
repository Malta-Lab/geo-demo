from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://46840eab91f15c1cec.gradio.live")

if __name__ == "__main__":
  app.run()
