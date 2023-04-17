from flask import Flask, render_template, redirect, session, request, url_for
import msal
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['TENANT_ID'] = os.getenv('TENANT_ID')
app.config['CLIENT_ID'] = os.getenv('CLIENT_ID')
app.config['CLIENT_SECRET'] = os.getenv('CLIENT_SECRET')
app.config['AUTHORITY'] = f"https://login.microsoftonline.com/{os.getenv('TENANT_ID')}"
app.config['SCOPE'] = ["User.ReadBasic.All"]
app.config['REDIRECT_PATH'] = "/authorized"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    msal_instance = msal.ConfidentialClientApplication(
        app.config['CLIENT_ID'], authority=app.config['AUTHORITY'],
        client_credential=app.config['CLIENT_SECRET']
    )

    auth_url = msal_instance.get_authorization_request_url(
        app.config['SCOPE'],
        redirect_uri=url_for('authorized', _external=True, _scheme='https')
    )
    return redirect(auth_url)

@app.route('/authorized')
def authorized():
    code = request.args.get('code')
    msal_instance = msal.ConfidentialClientApplication(
        app.config['CLIENT_ID'], authority=app.config['AUTHORITY'],
        client_credential=app.config['CLIENT_SECRET']
    )

    result = msal_instance.acquire_token_by_authorization_code(
        code, app.config['SCOPE'],
        redirect_uri=url_for('authorized', _external=True, _scheme='https')
    )

    if 'access_token' in result:
        session['user'] = result['id_token_claims']
        return redirect("http://10.0.6.85")
    else:
        return "Error: Access token not found."

@app.route('/profile')
def profile():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('profile.html', user=session['user'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
