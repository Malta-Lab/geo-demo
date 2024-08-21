from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://50b146aeb66da6ccda.gradio.live")

if __name__ == "__main__":
  app.run()
