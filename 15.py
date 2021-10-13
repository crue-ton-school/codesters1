stage.set_background("winter")
sprite = codesters.Sprite("fox")
sprite.move_down(150)
stage.wait(2)
sprite.move_right(50)
def click(sprite):
    sprite.say("Hello, Crue")
    # add other actions...
    
sprite.event_click(click)