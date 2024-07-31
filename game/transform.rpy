define _scene_show_hide_transition = dissolve

# 图像资源
image book = "Enchanted_Book.gif"

# 声音资源
define audio.knockdoor = "敲门.ogg"

define audio.us = "01-Unwelcome School.flac"
define audio.mc = "02. Midsummer cat.flac" # 清新活泼春天
define audio.sg = "03-Shady Girls.flac" # 幽默
define audio.at = "04. Alkaline Tears.flac" # 抒情
define audio.sstars = "04. Shooting Stars.flac"
define audio.lm = "05. Luminous Memory.flac"
define audio.cl = "06. Crucial Issue.flac" # 悬疑
define audio.ec = "06. Endless Carnival.flac" # 紧张黑白总力
define audio.fd = "06-Foolish Days.flac"
define audio.md = "07. Morose Dreamer.flac" # 抒情安静纯钢琴
define audio.ssometime = "10. someday, sometime.flac" # 同上爱丽丝
define audio.mo = "12. Moment.flac" # 同上yosuganosora
define audio.wd = "12. Water Drop.flac" # 高兴活力
define audio.ai = "13. Aira.flac" # 安静田园宁静舒服
define audio.sstory = "14. Sugar story.flac" # 夜晚安静
define audio.ws = "26-Welcome School.flac"

# 转场
transform left_to_right:
    xalign 0.0
    linear 2.0 xalign 1.0
    repeat

transform ariana.left:
    xcenter .3

