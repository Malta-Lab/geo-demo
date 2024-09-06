from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://78a193f0bbe38835da.gradio.live")

if __name__ == "__main__":
  app.run()
