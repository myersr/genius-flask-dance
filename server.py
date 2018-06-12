from flask import Flask, redirect, url_for, render_template
from flask_dance.consumer import OAuth2ConsumerBlueprint


app = Flask(__name__)
app.secret_key = "ssssh_secret"
example_blueprint = OAuth2ConsumerBlueprint(
    "genius-example", __name__,
    client_id="<client-id>",
    client_secret="<client-secret>",
    base_url="https://api.genius.com",
    token_url="https://api.genius.com/oauth/token",
    redirect_to="auth",
    scope = ["me"],
    authorization_url="https://api.genius.com/oauth/authorize",
)
app.register_blueprint(example_blueprint, url_prefix="/login")

@app.route("/auth")
def auth():
    resp=example_blueprint.session.get("/account")
    #assert resp.ok
    contentVal = resp.content
    return render_template('auth.html', cont=contentVal)


@app.route("/")
def index():
    if not authed():
        return redirect(url_for('genius-example.login'))
    resp = genius-example.get("/account")
    assert resp.ok
    return "Good"

def authed():
    resp = example_blueprint.session.get("/account")
    print(resp.ok)
    print("Here's the response content: " + resp.content)
    return False

if __name__ == "__main__":
    app.run()



