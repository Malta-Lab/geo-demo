from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://d977d58ebcd969669f.gradio.live")

if __name__ == "__main__":
  app.run()
