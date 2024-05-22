from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://6c08e6dda3e1eb370d.gradio.live")

if __name__ == "__main__":
  app.run()
