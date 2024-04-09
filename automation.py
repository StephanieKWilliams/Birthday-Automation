import datetime
import json
import pywhatkit as kit

def send_birthday_message(name, phone_number):
    message = f"Happy Birthday, {name}! 🎉"
    # The time is in 24-hour format
    # For example, 12:00 PM is 12:00, and 1:00 PM is 13:00
    # Adjust the time based on when you want to send the message
    kit.sendwhatmsg(phone_number, message, 12, 6) # Sends the message at 12:00 PM

def check_birthdays():
    today = datetime.date.today()
    with open('phone_numbers.json', 'r') as file:
        contacts = json.load(file)
    for contact in contacts:
        name = contact["name"]
        phone_number = contact["phone_number"]
        birthdate_str = contact["birthdate"]
        birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        if today == birthdate:
            send_birthday_message(name, phone_number)

if __name__ == "__main__":
    check_birthdays()
