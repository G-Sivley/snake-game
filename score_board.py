from turtle import Turtle


class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.read_highscore()
        
        # Set the position to the top of the screen
        self.setpos(x=0, y=270)
        self.update_score_board()
    
    def update_score_board(self):
        self.clear()
        message = f"Score: {self.score} Highscore: {self.high_score}"
        
        self.write(message, align="center", font=("Arial", 24, "normal"))
    
    def add_point(self):
        self.score += 1


    def update_highscore(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_highscore()

        self.score = 0
        self.update_score_board()

     
    def read_highscore(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())
    
    def write_highscore(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")