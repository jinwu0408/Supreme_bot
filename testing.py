from user import users
from config import profile_name
import urllib2

req = 'http://www.voidspace.org.uk'
response = urllib2.urlopen(req)
the_page = response.read()
print (the_page)


