import shutil
import re

def extract_email(from_path, to_path):
    """This will extract all the emails from a text document and write them to a new file, separated on there own line.
    """
    with open(from_path) as f:
        content = f.read()

        emails = re.findall(r'[\w-]+@[\w-]+\.(?:com|net|org|info)', content)
        unique_emails = list(set(emails))
        unique_emails.sort()

    with open(to_path, 'w+') as f:
        for email in unique_emails:
            f.write(email + '\n')

def extract_phone(from_path, to_path):
    """This will extract all the phone numbers from a text document and write them to a new file, separated on there own line.
    """
    with open(from_path) as f:
        content = f.read()

        #finds all phone numbers of 10 digits
        numbers = re.findall(r'\d{3}.\d{3}.\d{4}', content)
        numbers_striped = [num.replace(')', "-") for num in numbers]
        numbers_striped = [num.replace('.', '-') for num in numbers_striped]
     
        #finds all phone numbers 7 in a row
        numbers_seven = re.findall(r'\d{7}', content)
        formated_seven = []
        for num in numbers_seven:
            fixed = '206-'+num[0:3]+'-'+num[3:7]
            formated_seven.append(fixed)
        
        #combines both lists and sorts them
        phone_list = numbers_striped + formated_seven
        phone_list = list(set(phone_list))
        phone_list.sort()

    with open(to_path, 'w+') as f:
        for num in phone_list:
            f.write(num + '\n')

def extract_contact_info(from_path, to_path_email, to_path_phone):
    extract_email(from_path, to_path_email)
    extract_phone(from_path, to_path_phone)

document = './assets/potential-contacts.txt'
document2 = './assets/demo-document.txt'
email_path = './assets/emails.txt'
phone_path = './assets/phone_numbers.txt'

extract_contact_info(document2, email_path, phone_path)