import pico2d
import game_framework
import play_state
import logo_state
import item_state
import boy_adjust_state
#import boy_add_delete

pico2d.open_canvas()
game_framework.run(play_state)
#game_framework.run(item_state)

pico2d.close_canvas()

