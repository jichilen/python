import hashlib

md5=hashlib.md5()
db = {
        'michael': 'e10adc3949ba59abbe56e057f20f883e',
        'bob': '878ef96e86145580c38c87f0410ad153',
        'alice': '99b1c2188db85afee403b1536010c2c9'
    }

def calc_md5(password):
    if isinstance(password,str):
        md5.update(password)
        return md5.hexdigest()
    return null

def login(user,password):
    if db.has_key(user):
        pw=calc_md5(password)
        if db[user]==pw:
            return True
    return False

def main():
    name='michael'
    pw='123456'
    print login(name,pw)

if __name__ == '__main__':
	main()
