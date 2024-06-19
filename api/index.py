from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://8ce71a24730627926d.gradio.live")

if __name__ == "__main__":
  app.run()
