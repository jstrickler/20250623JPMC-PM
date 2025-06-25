
class Ghost:
    def frighten(self):
        print("BOOOOOO")

g = Ghost()
g.frighten()

class Spirit:
    def __call__(self):
        print("wooooOOOOOOoooo")

s = Spirit()
s()  # call the class instance