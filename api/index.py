from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://5931ee754773e06e7f.gradio.live")

if __name__ == "__main__":
  app.run()
