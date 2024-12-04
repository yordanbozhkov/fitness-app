class User:

    def __init__(self, name, age, weight, height, fitness_goal):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.fitness_goal = fitness_goal
        self.workout_history = []

    def update_weight(self, new_weight):
        self.weight = new_weight

    def update_height(self, new_height):
        self.height = new_height

    def update_goal(self, new_goal):
        self.fitness_goal = new_goal

    def log_workout(self, workout):
        self.workout_history.append(workout)

    def display_info(self):
        return f"Name: {self.name}\n Age: {self.age}\n Weight: {self.weight}\n Height: {self.height}\n Fitness Goal: {self.fitness_goal}"


user_name = input()
user_age = int(input())
user_weight = float(input())
user_height = int(input())
user_goal = input()

user = User(user_name, user_age, user_weight, user_height, user_goal)

print(user.display_info())

