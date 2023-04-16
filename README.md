# Flask Azure AD Login Sample App

This is a simple Flask web application that demonstrates how to authenticate users with Azure Active Directory (AD) and redirect them to a secured page after successful login. The application uses the Microsoft Authentication Library (MSAL) for Python to perform the authentication.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fuser%2Frepo%2Fmaster%2Fazuredeploy.json)

## Features

- Login with Azure AD
- Redirect to secured page after successful login
- Log out and clear session

## Prerequisites

- Python 3.8+
- Azure Subscription
- Azure Active Directory App Registration

## Setup

1. Clone the repository:

```
git clone https://github.com/your-github-username/flask-azure-ad-login.git
cd flask-azure-ad-login
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Create an Azure Active Directory App Registration in the [Azure Portal](https://portal.azure.com/).

4. Update the `app.config` values in `app.py` or use environment variables in Azure App Service for the following parameters:

- `CLIENT_ID`: Your Azure AD App Registration's client ID.
- `CLIENT_SECRET`: Your Azure AD App Registration's client secret.
- `TENANT_ID`: Your Azure AD tenant ID.

5. Run the application locally:

```python
python app.py
```

6. Access the application at `http://localhost:5000`.

## Deploy to Azure App Service

1. Create a new Web App in the [Azure Portal](https://portal.azure.com/).

2. In the Deployment Center, connect your Web App to the GitHub repository where this project is stored.

3. Configure the build provider to use Python and select the appropriate Python version.

4. Set the following environment variables in your Web App's "Configuration" settings:

- `CLIENT_ID`: Your Azure AD App Registration's client ID.
- `CLIENT_SECRET`: Your Azure AD App Registration's client secret.
- `TENANT_ID`: Your Azure AD tenant ID.

5. Trigger a new deployment in the Deployment Center or push a commit to the GitHub repository to start the deployment process.

6. Access the application using the Web App's URL.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.