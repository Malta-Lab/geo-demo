from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://4ae0b39e89a55045d7.gradio.live")

if __name__ == "__main__":
  app.run()
