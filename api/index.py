from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://c81176583ccb18df5d.gradio.live")

if __name__ == "__main__":
  app.run()
