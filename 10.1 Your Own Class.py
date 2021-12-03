'''
Michelle Sun
10.1 Your Own Class
Description:  implementation of a custom class that is based on a real-world object
Resources: 
https://realpython.com/instance-class-and-static-methods-demystified/,https://astronomy.swin.edu.au/cosmos/e/Ellipse,https://www.educative.io/edpresso/what-is-super-in-python, https://blog.finxter.com/solved-typeerror-method-takes-1-positional-argument-but-2-were-given/, https://www.google.com/search?q=smtp+server+for+gmail&rlz=1C1VDKB_enUS971US971&sxsrf=AOaemvIwW_7CU698p58iUDISX2RvPvIz2Q%3A1638438238232&ei=XpWoYe3CDdXQ9AOt8oOwBg&ved=0ahUKEwjt6bOJ6sT0AhVVKH0KHS35AGYQ4dUDCA8&uact=5&oq=smtp+server+for+gmail&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBQgAEIAEMgoIABCABBCHAhAUMgUIABCABDIFCAAQgAQyBQgAEIAEMgoIABCABBCHAhAUMgUIABCABDIFCAAQhgMyBQgAEIYDOgcIABBHELADOgcIABCwAxBDOgYIABAWEB46CAghEBYQHRAeSgQIQRgAUJwBWN8VYJMaaANwAngAgAGzAYgBpAqSAQQxMi4ymAEAoAEByAEKwAEB&sclient=gws-wiz, https://betterprogramming.pub/how-to-send-an-email-with-attachments-in-python-abe3b957ecf3, https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp, https://www.geeksforgeeks.org/getter-and-setter-in-python/ 
'''
# Imported from smtplib, MIMEMultipart, MIMEText for email method. 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Class for student info - Allows to get and change the student info and the info gets printed on a document, and then gets sent to specified email 
class Student_info:

# initalize the object's states
# I set everything to a default value. 
    def __init__(self, name = "Jett", phone = "0000000000", ID = 000000, gpa = 0):

# I made all of the variables private and set them to a variable name
        self._name = name
        self._ID = ID
        self._phone = phone
        self._gpa = gpa

# I made get functions for the Default name, ID, phone, gpa and returns a message that the Default choices has been aquired
    def get_name(self):
        return f"{self._name}'s Default name acquired."

    def get_ID(self):
        return f"{self._ID}\n Default ID acquired."

    def get_phone(self):
        return f"{self._phone}\n Default Phone number acquired."

    def get_gpa(self):
        return f"{self._gpa}\n Default GPA acquired."

# I made set functions for setting the name, ID, phone, gpa and return message that the information has been changed.
    def set_name(self, name):
        self._name = name
        return f"Name has been changed to {name}."

    def set_phone(self, phone):
        self._phone = phone
        return f"Phone number has been changed to {phone}."
    
    def set_ID(self, ID):
        self._ID = ID

# I made an if statement so that if the input was a string that can't be converted then it would throw an error. 
        if ID == int or float:
            ID = int(ID)
            return f"ID has been changed to {ID}."
        else: 
            return "Error"
    
    def set_gpa(self, gpa):
        self._gpa = gpa

# I made an if statement so that if the input was a string that can't be converted then it would throw an error
        if gpa == int or float: 
            gpa = float(gpa)
            return f"GPA has been changed to {gpa}."
        else: 
            return "Error"

# Creates a automatic text file of the student info
    def create_doc(self):

# takes user input for which student you are making the info for
        n = input("Enter Student Name: ")

# makes the file for the specified Student
        fg = open(f"{n}'s Final Grade", 'w')

# the actual writing part of the file with the format
        fg.write(f"Student Name: {self._name}\n \t ID#: {self._ID}\n \t Phone#: {self._phone}\n \t GPA: {self._gpa}")


# Takes user inputs and store them into variables.   
    your_email = input("Type in your email: ")
    your_password = input("Type in your email password: ")

# specify what server and port is being used for email engine
    server_info = smtplib.SMTP('smtp.gmail.com', 587)
    server_info.ehlo()

# Starts the connection to the STMP server to TLS mode
    server_info.starttls()

# takes user info to login to a STMP server for authentication
    server_info.login(your_email, your_password)

# Method to send mail
    def send_mail(self, body):

# ask for user info again to be able to actually send mail store the input in a variable for later use
        your_email = input("Type in your email again: ")
        your_password = input("Type in your password again: ")

# ask for the email they want to send their email to, store info into a variable for later use
        their_email = input("Type in the email you want this to be sent to: ")

# ask for the filename they want to send with the email, store into variable for later use
        filename = input("Enter File Name: ")

# Set MIMEMultipart to variable to use MIMEHeaders for the email, this which contains the subject, from, to, and body and attachments
        msg = MIMEMultipart()

# first define what the message subject will be and set string
        msg['Subject'] = 'Final Grades'

# define who this email is from which takes the user input from earlier
        msg['From'] = your_email

# define who this email is for which takes the user input for who they want to send to from earlier
        msg['To'] = their_email

# Use MIMEText to create the message you want to send and put it into a variable
        msgInfo = MIMEText(f"Here is {body}'s Final Grades and Student Info.")

# use the attach function to attach the message you want to send which was the variable before
        msg.attach(msgInfo)

# use the attach function to attach the file you want to send with MIMEText, which creates a document, but with the help of the open function and .read function it enables it open and attach the specified document from user input
        msg.attach(MIMEText(open(filename).read()))

# This part is if your authentication or connection doesn't work the program will automatically quit
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server_info:
                server_info.ehlo()
                server_info.starttls()
                server_info.login(your_email, your_password)
                server_info.sendmail(your_email, their_email, msg.as_string())
        except Exception as p:
            print(p)

# testing site
def main():
    e = Student_info(name = "Jett", phone = "0000000000", ID = 0, gpa = 0)
    print(e.get_name(), e.get_ID(), e.get_phone(), e.get_gpa())
    print(e.set_name("Jacob"), e.set_ID(123456), e.set_phone("(905)304-5689"), e.set_gpa(4.0))
    print(e.create_doc())
    e.send_mail("Jacob")
    
if __name__ == "__main__":
    main()
