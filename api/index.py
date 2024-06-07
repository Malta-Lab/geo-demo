from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://622e4aa65ecfc29d2e.gradio.live")

if __name__ == "__main__":
  app.run()
