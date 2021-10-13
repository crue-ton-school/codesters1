stage.set_background("winter")
sprite = codesters.Sprite("fox")
sprite.set_speed(2)
sprite.move_down(150)
stage.wait(1)
sprite.move_right(50)
sprite.say("Click on me!")


def click():
    sprite.say("Hey there Codester!")
    sprite.move_up(100)
    sprite.turn_right(360)
    sprite.move_down(100)
    sprite.say("Great job.")
    sprite.wait(2)
    sprite.say("Click submit and next to continue!")
sprite.event_click(click)