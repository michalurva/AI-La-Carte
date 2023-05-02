from api.google_api_authentication_client import GoogleOAuth2Client
from datetime import datetime, time, timedelta
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

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
        
    def create_meal_event(self, meal, meal_date):
        date_format = '%Y-%m-%d'
        meal_date_time = datetime.strptime(meal_date, date_format)
        event_start = datetime.combine(meal_date_time, time(hour=18))  # Assuming dinner time at 6 PM
        event_end = event_start + timedelta(minutes=meal.cook_time)
        
        event = {
            'summary': meal.name,
            'description': self.generate_meal_description(meal),
            'start': {
                'dateTime': event_start.isoformat(),
                'timeZone': 'America/Los_Angeles',  # Adjust this to your desired time zone
            },
            'end': {
                'dateTime': event_end.isoformat(),
                'timeZone': 'America/Los_Angeles',  # Adjust this to your desired time zone
            },
            'reminders': {
                'useDefault': True,
            },
        }
        
        created_event = self.create_event('primary', event)
        return created_event


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
        
    @staticmethod
    def generate_meal_description(meal):
        recipe_title = meal.name
        ingredients = meal.ingredients
        prep_steps = meal.prep_steps
        cook_time = meal.cook_time
        day =  "Sunday"

        # Split the ingredients into a list
        ingredient_list = ingredients

        # Split the prep steps into a list
        prep_step_list = prep_steps

        # Format the recipe
        formatted_recipe = f"{recipe_title}\n\nIngredients:\n"
        for ingredient in ingredient_list:
            formatted_recipe += f"- {ingredient}\n"

        formatted_recipe += f"\nPreparation Steps:\n"
        for step in prep_step_list:
            formatted_recipe += f"{step.strip()}\n"

        formatted_recipe += f"\nCook Time: {cook_time} minutes"

        return formatted_recipe