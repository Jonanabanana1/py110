# # Given this class:
# class Dog:
#     def speak(self):
#         return "bark!"

#     def sleep(self):
#         return "sleeping!"


# teddy = Dog()
# print(teddy.speak())  # bark!
# print(teddy.sleep())  # sleeping!


# # Create a subclass from Dog called Bulldog overriding the sleep method to return "snoring!"
# class Bulldog(Dog):
#     def sleep(self):
#         return "snoring!"


# karl = Bulldog()
# print(karl.speak())  # bark!
# print(karl.sleep())  # snoring!


class Animal:
    def speak(self):
        return "bark!"

    def sleep(self):
        return "sleeping!"

    def run(self):
        return "running!"

    def jump(self):
        return "jumping!"


# Let's create a few more methods for our Dog class.
class Dog:
    def fetch(self):
        return "fetching!"


# Create a new class called Cat, which can do everything a dog can, except fetch. Assume the methods do the exact same thing. Hint: don't copy and paste any methods from Dog into Cat; come up with a class hierarchy instead.
class Cat(Animal):
    pass
