from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://4b7a9948c479fe7a90.gradio.live")

if __name__ == "__main__":
  app.run()
