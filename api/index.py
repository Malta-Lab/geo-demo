from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://151036c0af9ab3f063.gradio.live")

if __name__ == "__main__":
  app.run()
