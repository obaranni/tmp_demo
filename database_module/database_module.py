import json

# module
module = "\n\n=======> Database <=======\n\n"

# methods
add_platform = "*** add_platform ***\n\n"
add_rules = "*** add_rules ***\n\n"
get_platform = "*** get_platform ***\n\n"
register_user = "*** register_user ***\n\n"
ger_user = "*** ger_user ***\n\n"
set_action = "*** set_action ***\n\n"
get_rules = "*** get_rules ***\n\n"

class Database():
    def __init__(self):
        self.platforms_array = []
        self.rules_array = []
        self.users_array = []
        self.actions_array = []
        self.register_array = []

    def add_platform(self, platform_data, key):
        platform_data['key'] = key
        print(module, add_platform, "Data: ", platform_data, sep="")
        self.platforms_array.append(platform_data)
        print(self.platforms_array)
        self.register("New platform connected with protocol", "-", "-", "-")
        return True
    
    def add_rules(self, action_rules):
        print(module, add_rules, "Data: ", action_rules, sep="")
        self.rules_array.append(action_rules)
        print(self.rules_array)
        self.register("New rule added: " + action_rules['action_name'], action_rules['platform_name'], "-", action_rules['reward'])
        return True

    def register_user(self, user_name):
        print(module, register_user, "Data: ", user_name, sep="")
        self.users_array.append(user_name)
        self.register("New user registred", "-", user_name['user_name'], "-")
        return True

    def get_user(self, user_name, straight=1):
        print(module, ger_user, "Data: ", user_name, sep="")
        if straight:
            self.register("Get user request", "-", user_name, "-")
        for item in self.users_array:
            if item['user_name'] == user_name:
                return item
        else:
            return None

    def get_platform(self, platform_name, straight=1):
        print(module, get_platform, "Data: ", platform_name, sep="")
        if straight:
            self.register("Get platform request", platform_name, "-", "-")
        for item in self.platforms_array:
            if item['platform_name'] == platform_name:
                return item
        else:
            return None

    def set_action(self, action_data):
        print(module, set_action, "Data: ", action_data, sep="")
        self.actions_array.append(action_data)
        print(self.actions_array)
        self.register(("New user action: " + action_data['action_name']), action_data['platform_name'], action_data['user_name'], action_data['reward'])
        return True
    
    def set_balance(self, user_name, balance):
        i = 0
        while i in range(0, len(self.users_array)):
            if self.users_array[i]['user_name'] == user_name:
                self.users_array[i]['balance'] = balance
                return True
            i += 1

    def get_rules(self, platform_name, straight=1):
        print(module, get_rules, "Data: ", platform_name, sep="")
        if straight:
            self.register("Get rules request", platform_name, "-", "-")
        for item in self.rules_array:
            if item['platform_name'] == platform_name:
                return item
        else:
            return None

    def register(self, descrition, platform, user, reward):
        id = len(self.register_array) + 8608
        self.register_array.append({"ID": id, "Description": descrition, "Platform": platform, "User": user, "Reward": reward})
    
    def get_registered_actions(self):
        return self.register_array