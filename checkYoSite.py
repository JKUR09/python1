import urllib

yo_API_token = "..."

hostName = "http://www.domainname.com"

replyCode = urllib.urlopen(hostName).getcode()

#check the response...
if replyCode == 200:
  print hostName, 'is up!'
else:
  print hostName, 'is down!'
  
yo_Data = urllib.urlencode({"api_token":yo_API_token})
yo = urllib.urlopen("http://api.justyo.co/yoall/",yo_Data)
