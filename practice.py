import hmac
import random
import hashlib

from string import letters


secret = 'sdfwef'

def make_secure_val(val):
	secured_value = hmac.new(secret, val).hexdigest()
	return '%s|%s' % (val, secured_value)


def check_secure_val(secure_val):
	val = secure_val.split('|')[0]
	if secure_val == make_secure_val(val):
		return val
	
def make_salt(length = 5):
	return ''.join(random.choice(letters) for x in xrange(length))


def make_pw_hash(name, pw, salt = None):
	if not salt:
		salt = make_salt()
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s,%s' % (salt, h)

def valid_pw(name, password, h):
	salt = h.split(',')[0]
	return h == make_pw_hash(name, password, salt)

def users_key(group = 'default'):
	return db.Key.from_path('users', group)

class User(db.Model)




print make_pw_hash('seho','123')
print valid_pw('seho','123', 'LaJYS,00a7bdf9457d8854510ea199dc5efc067cb81537c28122bcfacf1d2906303152' )


# secure_val has this form
# value|{{secured_value}}
# val is the value
# and the make_secure_val(val) is goint to make value|{{secured_value}}
# now and then check the secure_val and make_secure_val(val)