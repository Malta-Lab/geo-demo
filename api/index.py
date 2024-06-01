from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://05b2e42300af6adcf5.gradio.live")

if __name__ == "__main__":
  app.run()
