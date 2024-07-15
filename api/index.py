from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://69476d23ece90eb60b.gradio.live")

if __name__ == "__main__":
  app.run()
