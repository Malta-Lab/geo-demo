from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://4e55aab60a4e39395e.gradio.live")

if __name__ == "__main__":
  app.run()
