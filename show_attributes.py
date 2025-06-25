x = []

all_attributes = [a for a in dir(x) if not a.startswith("__")]
for attr_name in all_attributes:
    attr_value = getattr(x, attr_name)  # not x.attr_name
    attr_type = type(attr_value)
    print(f"{attr_name:12} {attr_type}")

x = []
if hasattr(x, "append"):
    x.append('spam')

class Dog:
    pass

d = Dog()

def make_sound(self):
    print("woof! woof!")

setattr(Dog, 'bark', make_sound)
d.bark()