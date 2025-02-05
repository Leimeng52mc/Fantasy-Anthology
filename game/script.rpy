﻿# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define m= Character("我")

# define kami = Character("神")

define shito = Character("巫女")

define lillian = Character("莉莉安")
define alice = Character("爱丽丝奶奶")
define orel = Character("奥列尔")
define abel = Character("阿贝尔")

define elena = Character("爱莲娜")

# 游戏在此开始。
label start:

    # # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # # （命名为 bg room.png 或 bg room.jpg）来显示。
    
    # scene bg blk w
    # "这是个关于虚拟与真实的故事"
    # "希望、爱、救赎，这是我始终欲图表达的"
    # "纵使，美好的祝愿也会以扭曲出现"

    # scene bg town
    # "这是一个无比平和的小镇，由于地处各大文化交界，这里对于宗教信仰、文化习惯，统统报以理解并支持的态度。"
    # "所以，对于那些想要换个口味生活，或是想要游历大陆的人，「哈尔希恩」镇永远是他的不二选择"
    # "无数曾经于此生活的人，都会向着他的邻居友人们赞叹着"
    # "那里温暖而宁静的四季，热情而好客的街坊，以及腼腆而又深情的少女。"
    # "这便是，誉为“幻想乡」的哈尔希恩镇"
    
    # scene bg destoryedworld
    # with fade
    # "这是一个糟糕透的世界，所谓的神明回归了我们的文明"
    # """起初，一切便是欣欣向荣：极高的生产力、近乎无穷的能源、取之不竭的资源，
    # 祂们将此带来我们的文明，他们向世界宣告自由与民主，
    # 他们告诉人类："""
    # "你们，迎来了光明。"
    # """人们不必为了生存而工作，所有的行为均出自本心。
    # 短时间内，我们迎来了史无前例的辉煌与光明。
    # 然而，阴暗亦随之诞生——"""
    # "堕落和懈怠侵蚀了人类的精神，毒品与色情摧毁了人类的肉体。"

    # # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # # eileen happy.png 的文件来将其替换掉。

    # scene bg hall
    # with fade
    # with Pause(1.0)

    # # 此处显示各行对话。

    # kami "所以在这里生活，就仿佛垫着《蒙娜丽莎》的吸海洛因"
    # kami "为什么不前往我们这里呢？"
    # kami "如此美好的世界，你真的未曾心动？"
    # show book
    # "空旷的大厅？传来了诱惑的话语。"
    # "在那话语的尽头，是本神圣洁白的书籍。"

    scene bg field
    play music mc
    "我呼吸这这里的空气，真觉得这将会是一场奇妙的旅行，或许我会喜欢上这里也说不定，但至少比……"
    "少女的声音" "「您好，远方而来的客人」"

    show lillian
    with moveinright
    "回头，转身，一位少女正躬腰向我行礼，动作行云流水，搭配上她的服饰，身份一目了然。"
    "女仆" "「此地的领主阿贝尔•德•哈尔西恩伯爵邀请您前往他的宅邸一叙」"
    "女仆" "「路途稍远，请跟紧我，此处的风景素来受到您这样的旅客赞美，希望您也能享受此处的风景」"
    m "「谢谢，但为什么阿贝尔伯爵会邀请我呢？」"
    show lillian #annoy
    "女仆" "「……不可直呼主人姓名，客人，此外，主人的意志我无从得知。」"
    m "「抱歉。」"
    hide lillian
    "一路上，我们不再交谈，尤其是当少女有着略微嗔怒之后。"
    "四周的风景的确不坏，当金黄色的光晕染这路旁的麦草，略带凉意的风轻抚我的发顶时，似乎连心中的不安也消散了。"

    play music md
    scene bg mansion night
    "路程比想象中稍远，当到达那座府邸时，天色也正好暗下来。"
    "温暖的火把代替的太阳，驱散了黑暗与凉气，也给这座庄园笼罩上一层神秘。"
    show lillian
    play sound knockdoor
    "噔噔噔。"
    "女仆叩响了大门的门环。"
    show lillian at left
    with move
    show orel at right
    with moveinright
    "一位管家模样的男子走来。"
    "男子" "「莉莉安小姐回来了啊。」"
    "男子" "「这位便是老爷提到的客人？」"
    "我才知道这位女仆的名字叫莉莉安，就听到她回应道"
    lillian "「是的，奥列尔先生，请让我们进去吧，别让主人久等了。」"
    orel "「好的，客人请进。」"
    m "「谢谢」"

    play music lm
    scene bg room
    with fade
    "随着庄园大门的打开，神秘背后的生气逐步显露出来。"
    "女仆们在忙来忙去，但她们的脸上并未露出麻木，尤其是那种外世界旧社会所描述的社畜模样。取而代之的是有说有笑，仿佛有什么喜事发生。"
    "我想起来现在外世界了，那个一直灰蒙蒙的地方。"
    "「或许连社畜都不如啊。」我这样觉得。这时我才注意到女仆们都有意无意的向我这边瞟着，眼睛里带着好奇与善意。"
    "我也不禁微笑起来，向她们点了点头。"

    scene bg dininghall
    with wiperight
    "继续跟着女仆走着，穿过一道又一道长廊，不多时，一个英伟的男人注意到了我，而我也立刻意识到他便是此地的主人。"
    show abel
    pause 1.0
    "男子" "「哦——，远方而来的客人，可算是把您等来了。」"
    "男子" "「我是阿贝尔•德•哈尔西恩，此地的领主，您称呼我为阿贝尔便好。」"
    m "「我叫林乐胥，出生于赤神。」"
    "这是我在大殿上，那本书赋予我的身份。本来也没期待什么，它能保证我原名不变就已经非常足够了。"
    abel "「啊，果然是勃艮第公爵特意让我照顾的林先生啊，有失远迎。」"
    m "「不必，能让您款待已经是我的荣幸了。」"
    "我尽量学习着他的语言习惯，觉得这些礼节真是十分麻烦。"
    "阿贝尔似乎看出来我对这种客套的不耐烦，便大手一挥，指挥起了仆人们。"
    abel "「好了，让我们开始我们今晚的迎新宴吧。」"
    "随即他让管家把我迎到了上座。"
    "果然，女仆们是在为我准备晚宴，先前的疑惑也得到了解答。"
    "晚宴很丰盛，或许是考虑到我是东方人，饭菜竟带有些许东方特色。"
    "我很好奇，为什么这个看上去的典型西方庄园会有东方厨师。但随即被美味征服，不再思考。"

    scene bg office
    with wiperight
    "晚宴后阿贝尔将我请到了书房。"
    show abel
    abel "「林先生在这里有什么打算？」"
    m "「我准备在这里生活一段时间。」"
    abel "「一年吗？」"
    "我惊讶于他很准确的猜出了我停留的时间，虽然这是那本书给我的体验时间。"
    m "「是的，阿贝尔先生，您的直觉非常准确。」"
    abel "「哈哈，这可不是直觉，大多数点名来到这里的客人，都会停留一年。」"
    m "「原来如此。」"
    abel "「你有什么打算吗？我们这里有三个可以提供住宿的地方。」"
    abel "「那些都是居民资源提供的住所，但前提是你需要为他们提供一些帮助。」"
    abel "「如果你是来享受宁静，神社提供了一个住所，那里在山腰，十分祥和。」"
    abel "「如果你是来体验小镇风土人情，酒馆的老板还有空的房间。」"
    abel "「当然，你如果单纯想换个地方住，我这里也很不错的。」"
    abel "「至于帮助，大概率是一份工作，别的我不清楚，但我这里就让你算算账。谁让你是勃艮第的朋友嘛，他的朋友，就是我的朋友。哈哈哈哈。」"
    "我静静地听着眼前英伟的领主变得话唠。"
    "「他真是个豪爽的人。」我这样想着。"
    abel "「所以，你选择哪个地方呢？」"

menu:
    "「所以，你选择哪个地方呢？」{fast}"
    "就在这里":
        jump maid
    "神社":
        jump shito
    "酒馆":
        jump boss

label ge:
    # 此处为游戏结尾。
    "{b}Good 结局{/b}"
    return