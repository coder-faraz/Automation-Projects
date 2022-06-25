#First, turn On 'Allow less secure app access'  &  Have an Internet Connection


import os.path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


my_email = 'farazhusain619@gmail.com'   # My e-mail address
my_password = "blessedwiththebest@1"    # My e-mail account pw

send_to_email = 'hfaraz316@gmail.com'   # Receiver's e-mail ID
subject = 'Just a test email'           # Subject of the e-mail you are sending

bodyHTML = "<p>Visit <a href='fallingfalling.com'> fallingfalling.com </a> to get amazed <span style='color: aqua'>& enjoy</span></p>"
    # I am including HTML & CSS in my e-mail message
bodyPlain = "Visit fallingfalling.com to get amazed & enjoy!"   # This is the 
                                                    # e-mail message

attachment_location = "C:/Users/Faraz/Downloads/microsoft-word.png" # attachment



msg = MIMEMultipart("alternative")
msg['From'] = my_email         # Storing Sender's email ID
msg['To'] = send_to_email      # Storing Receiver's email ID
msg['Subject'] = subject

msg.attach(MIMEText(bodyPlain, 'plain'))  # Attach the plain e-mail to MIMEMultipart
msg.attach(MIMEText(bodyHTML, 'html'))   # Attach email that contains html & css



    # Setup the Attachment file
filename = os.path.basename(attachment_location)    # Opening the file to be
attachment = open(attachment_location, "rb")        # sent

part = MIMEBase("application", "octet-stream")      # Instance of MIMEBase with 2
                      # parameters - Content-type major  &  Content-type minor

part.set_payload(attachment.read())    # To change the payload into encoded form

encoders.encode_base64(part)           # encode into base64

part.add_header("Content-Disposition", "attachment; filename= %s" % filename)

msg.attach(part)    # Adding the attachment to MIMEMultipart Object



    # Now, I am creating an SMTP session
server = smtplib.SMTP("smtp.gmail.com", 587) # Connect to Outgoing mail server
                                             # SMTP, using port 587

server.starttls()   # This will start TLS for security

server.login(msg['From'], my_password)  # Login to the SMTP server using your
                                        # account credentials

text = msg.as_string()    # Converting MIMEMultipart object to a string to send

server.sendmail(msg['From'], msg['To'], text)    # Send our email to the specified
                                                 # email address

server.quit()       # Logout of the e-mail server when done, Terminating session

