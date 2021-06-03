
import urllib
import urllib2

URL = "www.mypersonalhoneypotclickheretobefound.com"
U = "backups"
P = "uedfGDFwybg25fs6fkKI3jddgfHJWuJAVD2yheu2i3SGWMCKk"



params = {'param1': 'value1'}

req = urllib2.Request("http://someurl", urllib.urlencode(params))
res = urllib2.urlopen(req)

data = res.read()
