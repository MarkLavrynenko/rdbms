from base64 import b64encode
import hmac, hashlib
from credentials import *


with open("mypolicy.json", "r") as f:
	policy_text = f.read()
	policy = b64encode(policy_text)
	mac = b64encode(hmac.new(AWS_SECRET, policy, hashlib.sha1).digest())
	print(policy)
	print(mac)



