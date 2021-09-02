from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("courier",24,"normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,270)
        self.color("white")
        self.penup()
        self.total_score = 0
        self.show_score = self.write(f" Your Score : ", align=ALIGNEMENT, font=FONT)
        self.hideturtle()

    def set_score(self):
        self.clear()
        self.total_score += 1
        self.show_score = self.write(f" Your Score : {self.total_score} ", align=ALIGNEMENT, font=FONT)
        print(f"the score is {self.total_score}")

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNEMENT, font=FONT)
        return False