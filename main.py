import sender
import csv


def load_template():
    with open("template.txt", encoding="utf-8") as file:
        return file.read()


def sending_algo():
    service = sender.authenticate()
    with open("test.csv", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            body = load_template().format(contact=row["company"])
            print(row["company"])
            #print(row["email"])
            sender.send_email(service, row["email"], body)

sending_algo()


