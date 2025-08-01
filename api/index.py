from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://c007005011f4e45b74.gradio.live")

if __name__ == "__main__":
  app.run()
