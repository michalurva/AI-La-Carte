import datetime
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from api.google_api_authentication_client import GoogleOAuth2Client

class GoogleCalendarClient:
    def __init__(self, credentials_file, token_file, scopes):
        self.oauth2_client = GoogleOAuth2Client(credentials_file, token_file, scopes)
        self.service = self.get_service()

    def get_service(self):
        credentials = self.oauth2_client.get_credentials()
        service = build('calendar', 'v3', credentials=credentials)
        return service

    def get_calendar_list(self):
        try:
            now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            print('Getting the upcoming 10 events')
            events_result = self.service.events().list(calendarId='primary', timeMin=now,
                                                maxResults=10, singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items', [])
            return events
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None

    def create_event(self, calendar_id, event):
        try:
            created_event = self.service.events().insert(calendarId=calendar_id, body=event).execute()
            return created_event
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None

    def update_event(self, calendar_id, event_id, event):
        try:
            updated_event = self.service.events().update(calendarId=calendar_id, eventId=event_id, body=event).execute()
            return updated_event
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None

    def delete_event(self, calendar_id, event_id):
        try:
            self.service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
            return True
        except HttpError as error:
            print(f"An error occurred: {error}")
            return False
