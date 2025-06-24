from abc import ABCMeta, abstractmethod

class SpamBase(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

    def blah(self):
        print("Blah, blah blah")

class Toast(SpamBase):
    def foo(self):
        print("foo foo foo")
    
    def bar(self):
        print("bar bar bar")

t = Toast()
t.foo()
t.bar()
t.blah()