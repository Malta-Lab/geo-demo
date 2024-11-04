from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://status.gradio.app.")

if __name__ == "__main__":
  app.run()
