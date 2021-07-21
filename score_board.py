from turtle import Turtle


class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        
        # Set the position to the top of the screen
        self.setpos(x=0, y=270)
        self.update_score_board()
    
    def update_score_board(self):
        # clear the previous writing so it is not overlapping
        self.clear()
        message = f"Score: {self.score}"
        
        self.write(message, align="center", font=("Arial", 24, "normal"))
        self.score += 1
        
    
    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Arial", 42, "bold")) 
