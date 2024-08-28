from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://4524b595cf0410ad98.gradio.live")

if __name__ == "__main__":
  app.run()
