##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
import random
import smtplib
import pandas

letters_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

my_email = "biruhtesfaye2121@gmail.com"
my_password = "izspftroghtydydi"

data = pandas.read_csv("birthdays.csv")
data = data.to_dict(orient="records")
current_date = dt.datetime.now().date()

for item in data:
    date_item = dt.date(year=item["year"], month=item["month"], day=item["day"])

    if date_item.month == current_date.month and date_item.day == current_date.day:
        choosed_letter = random.choice(letters_list)
        receiver_email = item["email"]
        with open("letter_templates/"+choosed_letter, 'r') as letter_text:
            message = letter_text.read()
            message = message.replace("[NAME]", item["name"])
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.ehlo()
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=receiver_email,
                                    msg=f"Subject:Happy Birthday!\n\n{message}")






# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




