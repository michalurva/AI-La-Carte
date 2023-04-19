import csv
from models.week import Week

class CalendarCSVHandler:
    '''Handles CSV operations for Google Calendar events.'''

    @staticmethod
    def save_to_csv(week: Week, file_path: str):
        '''Save calendar events to a CSV file in Google Calendar format.'''
        with open(file_path, 'w', newline='', encoding="UTF-8") as csvfile:
            fieldnames = ['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time',
                          'All Day Event', 'Description', 'Location', 'Private']
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csv_writer.writeheader()

            for day in week.get_days_list():
                if day is None:
                    continue
                for meal in day.meals:
                    # Meal event
                    csv_writer.writerow({
                        'Subject': f'{meal.name} (Cooking)',
                        'Start Date': day.date.strftime('%m/%d/%Y'),
                        'Start Time': '',  # You can specify the start time, e.g., '6:00 PM'
                        'End Date': day.date.strftime('%m/%d/%Y'),
                        'End Time': '',  # You can specify the end time, e.g., '7:00 PM'
                        'All Day Event': 'False',
                        'Description': f'Cook {meal.name} for {meal.cook_time} minutes',
                        'Location': '',
                        'Private': 'True'
                    })

                    # Other events (e.g., defrosting) can be added similarly
                    # You will need to determine the appropriate date and time for these events
