from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://0bfc643e60ca56d992.gradio.live")

if __name__ == "__main__":
  app.run()
