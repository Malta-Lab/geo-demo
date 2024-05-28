from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://9039346ff32c181c3f.gradio.live")

if __name__ == "__main__":
  app.run()
