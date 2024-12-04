class Workout:
    def __init__(self, name):
        self.name = name
        self.exercises = []

    def add_exercise(self, exercise: str, sets: int, reps: int, rest_time: int) -> None:
        self.exercises.append({'exercise': exercise, 'sets': sets, 'reps': reps, 'rest': rest_time})

    def remove_exercise(self, exercise_name: str) -> None:
        self.exercises = [ex for ex in self.exercises if ex['exercise'].name != exercise_name]

    def view_workout(self) -> None:
        print(f'Workout: {self.name}')

        if not self.exercises:
            print('No exercises added to this workout yet.')

        for ex in self.exercises:
            print(f'{ex['exercise'].name}: {ex['sets']} sets, {ex['reps']} reps, {ex['rest']} seconds rest.')


workout_name = input("Type your workout: ")

workout = Workout(workout_name)
