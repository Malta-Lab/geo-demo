from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://48192176423c0381b9.gradio.live")

if __name__ == "__main__":
  app.run()
