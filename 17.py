stage.set_background("fall")
sprite = codesters.Sprite("fox")
sprite.move_down(150)
stage.wait(2)
sprite.move_left(50)
sprite.move_right(50)
def click(sprite):
    sprite.say("Hello")
    # add other actions...
    sprite.turn_right(90)
sprite.event_click(click)