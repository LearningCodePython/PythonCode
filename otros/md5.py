import hashlib

def hash (val):
    p_encode = val.encode('utf-8')
    h = hashlib.new("md5", p_encode)
    passwd = h.hexdigest()
    print (passwd)

hash("hola mundo")