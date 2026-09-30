import sender
import csv
import sys



def load_template(template):
    with open("template.txt", encoding="utf-8") as file:
        return file.read()


def sending_algo(subject, template, sending_list):
    service = sender.authenticate()
    with open(sending_list, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            body = load_template().format(contact=row["company"])
            print(row["company"])
            #print(row["email"])
            sender.send_email(service, row["email"], subject, body)


def main():
    if len(sys.argv) != 3:
        print("Error... Usage: main.py <template.txt> <list.csv>")
        exit()

    print("Welcome to the automated EMAIL sender")
    subject = input("\n\nWhat should the subject of the emails be?:   ")
    sending_algo(subject, sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()


