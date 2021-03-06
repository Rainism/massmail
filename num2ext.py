# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

# Define these once; use them twice!
strFrom = 'presidents_office@pcom.edu'
strTo = 'marcwe@pcom.edu'

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Holiday Greeting Card 2014'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

#msgText = MIMEText('This is the alternative plain text message.')
msgText = MIMEText('click on http://dev.pcom.edu/communications/marcom/presidentscard_2014/holidaycard_external_2014.html for the holiday greeting card')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
#msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')
msgText = MIMEText('<font color="blue">Please adjust your volume settings to hear sound.</font><br /><br /><a href="http://dev.pcom.edu/communications/marcom/presidentscard_2014/holidaycard_external_2014.html" target="_blank"><img src="cid:image1" width="425" height="406" /></a><br><br><a href ="mailto:president%27s_office@pcom.edu?subject=2014_card_remove">Please remove me from this list</a>', 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open('externalemail.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# Send the email (this example assumes SMTP authentication is required)
import smtplib
smtp = smtplib.SMTP()
smtp.connect('10.11.0.25', 25)
#smtp.login('exampleuser', 'examplepass')
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()