from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://2845baf2a7977c4d44.gradio.live")

if __name__ == "__main__":
  app.run()
