from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://4fa387af0600b67c93.gradio.live")

if __name__ == "__main__":
  app.run()
