from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://7a49e6d653680381a4.gradio.live")

if __name__ == "__main__":
  app.run()
