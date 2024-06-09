from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://4de34540040ab3c654.gradio.live")

if __name__ == "__main__":
  app.run()
