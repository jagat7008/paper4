def generate_email(username,department):
    email_prefix= username.capitalize()+ '.' +department.lower()+'@'
    email_id=email_prefix+'gmail.com'
    return email_id
username='msys'
department='automation'
email_id=generate_email(username,department)
print(email_id)