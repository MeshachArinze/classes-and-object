class Student:
    # [assignment] Skeleton class. Add your code here
    name = "Ekene"
    age = 10
    tracks = ["ui/ux"]
    score = None

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def add_track(self, tracks):
        self.track = tracks

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score
    def __init__(self, name , age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.set_score(3)

print('name: ', Bob.name)
print('age: ', Bob.age)
print('tracks: ', Bob.tracks)
print('score: ', Bob.get_score())


# class Student:
     
#     # A simple class
#     # attribute
#     name = "student"
 
#     # A sample method 
#     def fun(self):
#         print("I'm a", self.name)
 
# # Driver code
# # Object instantiation
# Rodger = Student()
 
# # Accessing class attributes
# # and method through objects
# Rodger.fun()