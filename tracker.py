import time

class PerformanceTracker:
    def __init__(self):
        self.records = []   # Stores each question attempt

    def start_timer(self):
        """Start measuring response time."""
        self.start_time = time.time()

    def stop_timer(self):
        """Stop measuring and return time taken."""
        end_time = time.time()
        return round(end_time - self.start_time, 2)

    def log_result(self, correct, time_taken, difficulty):
        """
        Store each puzzle attempt.
        correct: bool
        time_taken: float
        difficulty: str
        """
        self.records.append({
            "correct": correct,
            "time": time_taken,
            "difficulty": difficulty
        })

    def get_summary(self):
        """Compute final session summary."""

        if not self.records:
            return {
                "accuracy": 0,
                "avg_time": 0,
                "total_questions": 0
            }

        total = len(self.records)
        correct_answers = sum(1 for r in self.records if r["correct"])
        avg_time = sum(r["time"] for r in self.records) / total

        return {
            "accuracy": round((correct_answers / total) * 100, 2),
            "avg_time": round(avg_time, 2),
            "total_questions": total
        }
