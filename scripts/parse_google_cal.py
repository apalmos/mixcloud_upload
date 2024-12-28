"""parse a Google calendar"""

import pandas as pd
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os
import datetime

# Define the scope for Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def authenticate_google_calendar():
    """Authenticate and return Google Calendar API service."""
    creds = None
    # Check if token.json exists (to avoid re-authentication)
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no valid credentials, authenticate the user
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for future use
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('calendar', 'v3', credentials=creds)

def fetch_calendar_events(service, calendar_id='primary'):
    """Fetch events from the specified calendar."""
    # Get events from now onwards
    now = f'{datetime.datetime.now(datetime.timezone.utc).isoformat()}Z'
    events_result = service.events().list(
        calendarId=calendar_id, timeMin=now,
        maxResults=100, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])
    return events

def events_to_dataframe(events):
    """Convert Google Calendar events to a Pandas DataFrame."""
    data = [
        {
            'Start': event['start'].get(
                'dateTime', event['start'].get('date')
            ),
            'End': event['end'].get('dateTime', event['end'].get('date')),
            'Summary': event.get('summary', 'No Title'),
            'Description': event.get('description', ''),
            'Location': event.get('location', ''),
        }
        for event in events
    ]
    return pd.DataFrame(data)

# Authenticate and fetch events
service = authenticate_google_calendar()
events = fetch_calendar_events(service)

# Convert events to a DataFrame
df = events_to_dataframe(events)

# Display the DataFrame
print(df)
