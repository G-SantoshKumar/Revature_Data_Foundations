import re 
def is_valid_email(email):
    pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern,email) is not None

def valid_email(email_list):
    return [email for email in email_list if is_valid_email(email)]

email_list = [
    "valid.email@example.com",
    "invalid-email.com",
    "another.valid@email.org",
    "bad@com",
    "user@domain.co.uk"
]
valid_emails=valid_email(email_list)
print(valid_emails)