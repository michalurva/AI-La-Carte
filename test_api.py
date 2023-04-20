from api.google_api_calendar_client import GoogleCalendarClient

def main():
    calendar_client = GoogleCalendarClient("credentials.json",
                                           "token.json",
                                           ["https://www.googleapis.com/auth/calendar"])

    calendar_list = calendar_client.get_calendar_list()
    print(f"Calendar list: {calendar_list}")

if __name__ == "__main__":
    main()
