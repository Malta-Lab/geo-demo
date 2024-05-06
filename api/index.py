from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://5b8cfc29dfa2a726e2.gradio.live")

if __name__ == "__main__":
  app.run()
