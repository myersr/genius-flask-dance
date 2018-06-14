from flask import Flask, redirect, url_for, render_template
from flask_dance.consumer import OAuth2ConsumerBlueprint
import os,json


#Function to determine if the user is authenticated
#  Makes a request to Genius at the account endpoint
#  If the request succeeds then the user is already 
#  logged in and the credentials are stored in the
#  session.
def authed():
    resp = example_blueprint.session.get("/account")
    responseSucc = resp.ok
    #print("Here's the response content: " + resp.content)
    return responseSucc

#Check to see that an input is not "None"
def envIsNotSet(envir):
    return envir is None


#initialize the application
app = Flask(__name__)
#In order to use session you must set an application secret
app.secret_key = "ssssh_secret"

#Grab the credentials from environment variables
geniusId = os.environ.get('GENIUS_ID')
geniusSec = os.environ.get('GENIUS_SEC')


#bootstrap the variables flask dance uses to do the Oauth2 dance
#http://flask-dance.readthedocs.io/en/latest/providers.html#custom
example_blueprint = OAuth2ConsumerBlueprint(
    "genius-example", __name__,
    client_id=geniusId,
    client_secret=geniusSec,
    base_url="https://api.genius.com",
    token_url="https://api.genius.com/oauth/token",
    redirect_to="auth",
    scope = ["me"],
    authorization_url="https://api.genius.com/oauth/authorize",
)
#Register the Flask blueprint
#http://flask.pocoo.org/docs/1.0/blueprints/
app.register_blueprint(example_blueprint, url_prefix="/login")

#The route that flask dance finally redirects you to after the dance is complete
@app.route("/auth")
def auth():
    #After authentication we hit the Genius api to grab account information
    resp=example_blueprint.session.get("/account")
    #Attempt and confirming we can get account info
    #assert resp.ok
    #Set variable to the returned account info
    contentVal = resp.content
    #Reder a Jinja template and pass the account info as variable cont.
    #auth.html is under templates/auth.html
    return render_template('auth.html', cont=contentVal)


#Base route for the flask server
@app.route("/")
def index():
    #Want to check and see if the user is authenticated as they hit the landing page
    if not authed():
        #Redirect the user to the login page registered under the genius-example blueprint if not authed
        return redirect(url_for('genius-example.login'))
    #If the user is authed we make a request to the Genius account api
    resp = example_blueprint.session.get("/account")
    #Check if the request is successful
    if not resp.ok:
        return redirect(url_for('genius-example.login'))
    #Last check. Should have caught it by now
    assert resp.ok
    #Serialize the Json response
    userInfo = json.loads(resp.content)
    #print(userInfo["response"])
    return "Hello " + userInfo["response"]["user"]["name"]


if __name__ == "__main__":
    # Check if Genius developer credentials are set and raise error if they aren't
    if (envIsNotSet(geniusId) or envIsNotSet(geniusSec)):
        print("""
        Missing Genius credentials. 
        Please set the environment variables GENIUS_ID and/or GENIUS_SEC.
        """)
        raise RuntimeError('Environment variables not set')
    #Start the Flask server
    app.run()


