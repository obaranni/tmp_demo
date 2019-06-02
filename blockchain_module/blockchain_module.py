import hashlib

# module
module = "\n\n=======> Blockchain <=======\n\n"

# methods
create_key = "*** create_key ***\n\n"

class Blockchain():
    def __init__(self):
        pass
    
    def create_key(self, user_name):
        print(module, create_key, "Data: ", user_name, sep="")
        user_key = hashlib.sha224(str.encode(user_name)).hexdigest()
        print(user_key)
        return user_key