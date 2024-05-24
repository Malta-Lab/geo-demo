from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://e4d6a62d895117993b.gradio.live")

if __name__ == "__main__":
  app.run()
