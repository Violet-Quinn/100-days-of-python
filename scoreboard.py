from turtle import Turtle
from select import select

ALIGNMENT="center"
FONT=("Arial",24,"normal")




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("snake_game_score.txt") as file:
            self.highscore=int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("snake_game_score.txt") as file:
                file.write(self.highscore)
        self.score=0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align=ALIGNMENT,font=FONT)
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()