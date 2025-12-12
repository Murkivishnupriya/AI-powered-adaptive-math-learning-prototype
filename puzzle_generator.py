import random

class PuzzleGenerator:
    def __init__(self):
        self.operations = ["+", "-", "*", "/"]

    def generate(self, difficulty):
        """
        Generates a math puzzle based on difficulty level.
        Returns:
            problem (str): e.g., "5 + 3"
            answer (float/int): correct answer
        """

        # Difficulty ranges
        if difficulty == "Easy":
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)

        elif difficulty == "Medium":
            num1 = random.randint(10, 50)
            num2 = random.randint(10, 50)

        elif difficulty == "Hard":
            num1 = random.randint(50, 150)
            num2 = random.randint(50, 150)

        else:
            raise ValueError("Invalid difficulty level")

        operation = random.choice(self.operations)

        # Avoid division by zero
        if operation == "/":
            num2 = random.randint(1, 10)

        problem = f"{num1} {operation} {num2}"
        answer = self.compute_answer(num1, num2, operation)

        return problem, answer

    @staticmethod
    def compute_answer(a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return round(a / b, 2)  # keep division answers clean
