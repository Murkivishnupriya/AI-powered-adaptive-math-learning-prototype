class AdaptiveEngine:
    def __init__(self):
        self.levels = ["Easy", "Medium", "Hard"]
        self.current_level = "Easy"
        self.performance_trend = 0  # + for correct, - for incorrect

    def update(self, correct):
        """
        Update difficulty trend based on performance.
        correct: bool
        """
        # Update trend
        if correct:
            self.performance_trend += 1
        else:
            self.performance_trend -= 1

        # Check if we need to change difficulty
        if self.performance_trend >= 2:
            self.increase_difficulty()
            self.performance_trend = 0  # reset trend

        elif self.performance_trend <= -2:
            self.decrease_difficulty()
            self.performance_trend = 0  # reset trend

        return self.current_level

    def increase_difficulty(self):
        idx = self.levels.index(self.current_level)
        if idx < len(self.levels) - 1:
            self.current_level = self.levels[idx + 1]

    def decrease_difficulty(self):
        idx = self.levels.index(self.current_level)
        if idx > 0:
            self.current_level = self.levels[idx - 1]

    def get_level(self):
        return self.current_level
