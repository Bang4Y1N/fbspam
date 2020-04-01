#coded by : salismazaya
#edited by : Bang4Y1N
try:
	import requests as r
except:
	print "[+] Can't import requests module"
	exit()

print "\033[92mFacebook Comment Spammer\nBy: Bang4Y1N\n\033[0m"
#login
t = raw_input("[?] Your Facebook Token: ")
if "error" in r.get("https://graph.facebook.com/me?access_token="+t).content:
	print "[+] Token Invalid !"
	exit()
print "[+] Login Success !"
id = raw_input("[?] Post Id: ")
if "error" in r.get("https://graph.facebook.com/"+id+"?access_token="+t).content:
	print "[+] Post Id Not Found"
	exit()

#spam
kata = raw_input("[?] Text Comment: ")
jumlah = int(input("[?] How Many: "))
print ""
try:
	for s in range(jumlah):
		post = r.get("https://graph.facebook.com/"+id+"/comments?method=POST&message="+kata+"&access_token="+t)
		print "[+] Comment Working To: " + str(s)
except:
	print "[+] Error!"
	exit()
		
