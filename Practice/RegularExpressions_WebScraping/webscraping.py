# Webscraping: Collecting information from webpages
# getting email Ids from jntuh website

import re
import urllib
import urllib.request
patterns = "[a-zA-Z0-9.]+@jntuh[.]ac[.]in"
site = 'https://jntuh.ac.in/contact-us'
response = urllib.request.urlopen(site)
text=response.read() # byte type
s_text = str(text) # converting into str

mail_IDs=set(re.findall(patterns,s_text)) # finding emailIds and converting them into set
for mail_id in mail_IDs:
  print(mail_id)
  