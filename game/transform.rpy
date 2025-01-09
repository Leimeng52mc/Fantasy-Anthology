define _scene_show_hide_transition = dissolve

# 转场
transform left_to_right:
    xalign 0.0
    linear 2.0 xalign 1.0
    repeat

transform ariana.left:
    xcenter .3

transform ariana.right:
    xcenter .7

transform flashwhite:
    white
    alpha 1.0
    linear 0.5 alpha 0.0

transform flashblack:
    black
    alpha 1.0
    linear 0.5 alpha 0.0

transform flashred:
    red
    alpha 1.0
    linear 0.5 alpha 0.0