class Stats():
    """Отслеживание статистики"""


    def __init__(self):
        """инициализирует статистику"""
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """статистика изменяющая во время игры"""
        self.guns_left = 2
        self.score = 0