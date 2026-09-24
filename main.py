import sender
import csv


def load_template():
    with open("template.txt", encoding="utf-8") as file:
        return file.read()


def sending_algo(subject):
    service = sender.authenticate()
    with open("test.csv", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            body = load_template().format(contact=row["company"])
            print(row["company"])
            #print(row["email"])
            sender.send_email(service, row["email"], subject, body)


def main():
    print("Welcome to the automated EMAIL sender")
    subject = input("\n\nWhat should the subject of the emails be?:   ")
    sending_algo(subject)

if __name__ == "__main__":
    main()


