from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://6a22045aaa6a532db1.gradio.live")

if __name__ == "__main__":
  app.run()
