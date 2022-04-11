#  https://www.codewars.com/kata/53f0f358b9cb376eca001079/train/python
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


ball1 = Ball()
ball2 = Ball("round")
print(ball1.ball_type)
print(ball2.ball_type)
