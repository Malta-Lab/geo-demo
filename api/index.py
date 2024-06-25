from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://fbe7bc82cda1d14a7b.gradio.live")

if __name__ == "__main__":
  app.run()
