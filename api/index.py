from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://b720a3ea8ec49e1512.gradio.live")

if __name__ == "__main__":
  app.run()
