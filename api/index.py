from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://2dfd377413157d75df.gradio.live")

if __name__ == "__main__":
  app.run()
