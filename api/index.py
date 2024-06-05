from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://9697b43a1890047f7b.gradio.live")

if __name__ == "__main__":
  app.run()
