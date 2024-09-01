from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://48abb15c8744d47c57.gradio.live")

if __name__ == "__main__":
  app.run()
