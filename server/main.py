# create a credential
from googleapiclient.discovery import build
from google.auth.transport import requests

# provides credentials based on OAuth 2.0 access and refresh tokens.
# These credentials usually access resources on behalf of a user
# Obtaining the initial access and refresh token is outside of the scope of this module
from google.oauth2 import credentials

from flask_cors import CORS
import flask
import os

# secret file to https://console.cloud.google.com/
CLIENT_SECRETS_FILE = "client_secret.json"

# define api scopes
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']

# which api and its version
API_SERVICE_NAME = 'people'
API_VERSION = 'v1'


app = flask.Flask(__name__)
CORS(app)


@app.route('/', methods=["POST"])
def home():
    try:
        # userAccessToken
        accessToken = flask.request.headers.get('accessToken')

        # userRefreshToken
        refreshToken = flask.request.headers.get('refreshToken')

        # credentialAccessToken
        token = flask.request.headers.get('token')

        # replace with client secret values and tokens
        cred = credentials.Credentials(
            token=None,
            id_token=None,
            refresh_token=None,
            token_uri=None,
            client_id=None,
            client_secret=None,
            scopes=SCOPES,
        )

        # service build object
        peopleApiService = build(
            API_SERVICE_NAME, API_VERSION, credentials=cred)

        # collection
        contactListResponse = peopleApiService.people().connections().list(
            # list creates a http request object
            resourceName='people/me',
            personFields='names,emailAddresses,phoneNumbers,photos,relations,urls'
            # call 'execute' to execute the request XD
        ).execute()

        # keys to search in the dictionarie: contactListResponse
        attributes = ["names", "photos", "phoneNumbers"]

        result = []
        temp = {
            "name": None,
            "photo": None,
            "phone": None
        }

        for contact in contactListResponse["connections"]:
            for item in attributes:
                if item in contact:
                    if item == "names":
                        temp["name"] = contact[item][0].get("displayName")
                    elif item == "photos":
                        temp["photo"] = contact[item][0].get("url")
                    elif item == "phoneNumbers":
                        temp["phone"] = contact[item][0].get("value")
            result.append(temp.copy())

        return flask.jsonify(result)
    except ValueError as error:
        print(error)
        return "error"


if __name__ == '__main__':
    # When running locally, disable OAuthlib's HTTPs verification.
    # turn it off in production.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    app.run('127.0.0.1', 5000, debug=True)
