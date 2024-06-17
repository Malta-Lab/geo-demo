from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://a68f4367351b8e3536.gradio.live")

if __name__ == "__main__":
  app.run()
