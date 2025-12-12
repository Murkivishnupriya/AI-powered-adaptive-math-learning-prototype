from puzzle_generator import PuzzleGenerator
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

def main():
    print("\nWelcome to the AI-Powered Math Learning System.")
    user = input("Please enter your name: ")

    print("\nSelect your starting difficulty level:")
    print("1. Easy\n2. Medium\n3. Hard")
    
    choice = input("Enter 1, 2, or 3: ")

    difficulty_map = {"1": "Easy", "2": "Medium", "3": "Hard"}
    difficulty = difficulty_map.get(choice, "Easy")

    print(f"\nThank you, {user}. Starting with {difficulty} difficulty.\n")

    pg = PuzzleGenerator()
    tracker = PerformanceTracker()
    engine = AdaptiveEngine()
    engine.current_level = difficulty  # Apply selected starting level

    for i in range(5):  # ask 5 questions for the session
        print(f"\nQuestion {i+1}")

        # Generate puzzle
        problem, answer = pg.generate(engine.get_level())
        print(f"Solve: {problem}")

        # Track time
        tracker.start_timer()
        user_answer = input("Your answer: ")
        time_taken = tracker.stop_timer()

        # Validate response
        try:
            correct = float(user_answer) == float(answer)
        except:
            correct = False

        tracker.log_result(correct, time_taken, engine.get_level())

        # Display result
        if correct:
            print("Correct.")
        else:
            print(f"Incorrect. The correct answer is: {answer}")

        # Adaptive difficulty update
        new_level = engine.update(correct)
        print(f"Next difficulty level: {new_level}")

    # Final session summary
    summary = tracker.get_summary()

    print("\n----- SESSION SUMMARY -----")
    print(f"Total Questions: {summary['total_questions']}")
    print(f"Accuracy: {summary['accuracy']}%")
    print(f"Average Response Time: {summary['avg_time']} seconds")
    print("----------------------------")
    print("\nThank you for participating. See you next time.")

if __name__ == "__main__":
    main()
