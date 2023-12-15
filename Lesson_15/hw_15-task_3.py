# Lesson 15 Homework; Task 3

# Create a simple prototype of a TV controller in Python. It’ll use the following commands:

# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
#                    if the channel N or 'name' exists in the list, or "No" - in the other case.

# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.

class TVController:
    
    channels_list = [
        "BBC One",
        "BBC Two",
        "ITV",
        "Channel 4",
        "Channel 5",
        "TF1",
        "France 2",
        "ARD",
        "ZDF",
        "RTL",
        "ProSieben",
        "Canal+",
        "RAI",
        "Mediaset",
        "SVT1"
    ]

    current_channel = 1

    def first_channel(self):
        self.current_channel = 1
        return self.current_channel
    
    def last_channel(self):
        self.current_channel = len(self.channels_list)
        return self.current_channel
    
    def turn_channel(self, num):
        for index, channel in enumerate(self.channels_list):
            if num == index + 1:
                self.current_channel = num
                return self.current_channel
        return "Channel is out of range."
    
    def next_channel(self):
        for el in enumerate(self.channels_list):
            if self.current_channel == len(self.channels_list):
                return self.first_channel()
            else:
                self.current_channel += 1
                return self.current_channel
    
    def previous_channel(self):
        for el in enumerate(self.channels_list):
            if self.current_channel == 1:
                return self.last_channel()
            else:
                self.current_channel -= 1
                return self.current_channel
    
    def curr_channel(self):
        for el in enumerate(self.channels_list):
            return self.channels_list[self.current_channel-1]
        
    def exists(self, x):            # x may be name or number
        if type(x) == int:
            for index, channel in enumerate(self.channels_list):
                if x == index + 1:
                    return "Yes"
            else:
                return "No"
        elif type(x) == str:
            for el in self.channels_list:
                if x == el:
                    return "Yes"
            else:
                return "No"
        else:
            return "Unknown symbol"        
        
controller = TVController()

print(controller.next_channel())        # 2 
print(controller.first_channel())       # 1
print(controller.last_channel())        # 15
print(controller.next_channel())        # 1
print(controller.next_channel())        # 2
print(controller.next_channel())        # 3
print(controller.last_channel())        # 15
print(controller.previous_channel())    # 14
print(controller.previous_channel())    # 13
print(controller.previous_channel())    # 12
print(controller.curr_channel())        # Canal+
print(controller.previous_channel())    # 11
print(controller.previous_channel())    # 10
print(controller.curr_channel())        # RTL
print(controller.turn_channel(6))       # 6
print(controller.turn_channel(4))       # 4
print(controller.next_channel())        # 5 
print(controller.exists(13))            # Yes
print(controller.previous_channel())    # 4
print(controller.curr_channel())        # Channel 4
print(controller.exists(16))            # No
print(controller.exists("TET"))         # No
print(controller.exists("ProSieben"))   # Yes