from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://eea0caf21c47845b94.gradio.live")

if __name__ == "__main__":
  app.run()
