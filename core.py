import json
from blockchain_module.blockchain_module import Blockchain
from database_module.database_module import Database

# good responses
access_key = {"status": "success", "key":""}
success = {"status": "success"}

# bad responses
bad_data = {"status": "failed", "error": "bad data"}
not_found = {"status": "failed", "error": "not found"}

# module
module = "=======> Core <=======\n\n"

# methods
register_new_platform_method = "*** register_new_platform ***\n\n"
set_action_rules = "*** set_action_rules ***\n\n"
register_new_user = "*** register_new_user ***\n\n"
get_user_info_by_name = "*** get_user_key_by_id ***\n\n"
get_platform_info = "*** get_platform_info ***\n\n"
get_action_rules = "*** get_action_rules ***\n\n"
new_action  = "*** new_action ***\n\n"

# {"action": "test passed", "user_key": "142124192418"}

class Core:
    def __init__(self):
        self.blockchain_module = Blockchain()
        self.database_module = Database()
    
    def register_new_platform(self, platform_data):
        try:
            print(module, register_new_platform_method, "Data: ", platform_data, sep="")
            data = json.loads(platform_data)
            if self.database_module.get_platform(data['platform_name'], 0) != None:
                print("Already Exist!")
                raise
            result = access_key
            result['key'] = data['platform_name']
            self.database_module.add_platform(data, data['platform_name'])
        except:
            result = bad_data
        return result
    
    def set_action_rules(self, action_rules):
        try:
            print(module, set_action_rules, "Data: ", action_rules, sep="")
            data = json.loads(action_rules)
            if self.database_module.get_platform(data['platform_name'], 0) == None:
                raise
            data['action_name']
            data['reward']
            self.database_module.add_rules(data)
            result = success
        except:
            result = bad_data
        return result

    def register_new_user(self, user_name):
        try:
            print(module, register_new_user, "Data: ", user_name, sep="")
            data = json.loads(user_name)
            if self.database_module.get_user(data['user_name'], 0) != None:
                print("Already Exist!")
                raise
            user_key = self.blockchain_module.create_key(data['user_name'])
            result = {'user_name': data['user_name'], "user_pub_key": user_key, "balance": "0"}
            self.database_module.register_user(result)
        except:
            result = bad_data
        return result

    def get_user_info_by_name(self, user_name):
        try:
            print(module, get_user_info_by_name, "Data: ", user_name, sep="")
            data = json.loads(user_name)
            result = self.database_module.get_user(data['user_name'], 0)
            if result == None:
                raise
        except:
            result = not_found
        return result

    def get_platform_info(self, platform_name):
        try:
            print(module, get_platform_info, "Data: ", platform_name, sep="")
            data = json.loads(platform_name)
            platform_info = self.database_module.get_platform(data['platform_name'])
            if platform_info == None:
                raise
            result = platform_info
        except:
            result = not_found
        return result

    def get_action_rules(self, platform_name):
        try:
            print(module, get_action_rules, "Data: ", platform_name, sep="")
            data = json.loads(platform_name)
            result = self.database_module.get_rules(data['platform_name'])
            if result == None:
                raise
        except:
            result = not_found
        return result
    
    def new_action(self, action_data):
        try:
            print(module, new_action, "Data: ", action_data, sep="")
            action_data = json.loads(action_data)
            if self.database_module.get_platform(action_data['platform_name'], 0) == None or \
                self.database_module.get_user(action_data['user_name'], 0) == None or \
                    self.database_module.get_rules(action_data['platform_name'], 0)['action_name'] != \
                         action_data['action_name']:
                raise
            old_balance = self.database_module.get_user(action_data['user_name'])['balance']
            action_data['reward'] = self.database_module.get_rules(action_data['platform_name'], 0)['reward']
            self.database_module.set_action(action_data)
            self.database_module.set_balance(action_data['user_name'], int(old_balance) + int(action_data['reward']))
            result = success
        except:
            result = bad_data
        return result

    def get_user_balance(self, user_name):
        result = self.get_user_info_by_name(user_name)
        if result == not_found:
            return result
        return {"balance": result['balance']}
    
    def get_registered_actions(self):
        return self.database_module.get_registered_actions()