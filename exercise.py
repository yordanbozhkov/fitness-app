class Exercise:
    def __init__(self, name, description, weight, difficulty):
        self.name = name
        self.description = description
        self.weight = weight
        self.difficulty = difficulty

    def display_exercise(self):
        return (f'Exercise: {self.name} \n'
                f'Description: {self.description} \n'
                f'Weight: {self.weight} \n'
                f'Difficulty: {self.difficulty}')


exercise_name = input('Exercise: ')
exercise_description = input('Short Description: ')
exercise_weight = input('Weight Chosen: ')
exercise_difficulty = input('Difficulty: ')

exercise = Exercise(exercise_name, exercise_description, exercise_weight, exercise_difficulty)

print(exercise.display_exercise())
