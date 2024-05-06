from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://d34f864f3065344f35.gradio.live")

if __name__ == "__main__":
  app.run()
