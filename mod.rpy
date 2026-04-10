define s = Character("Сайори")
define y = Character("Юри")
define n = Character("Нацуки")
define m = Character("Моника")
define mc = Character("[player]")
define u = Character("???")

default poems2_shared = 0
default sayori2_done = False
default natsuki2_done = False
default yuri2_done = False
default monika2_done = False

label mod:
    scene bg residential_day with wipeleft_scene
    pause(0.1)
    play music t2
    "Я, как обычно, шёл в школу не подозревая что что-то может пойти не так."
    "Внезапно я услышал звуки сирены позади меня."
    "Я бы испугался, если бы это случилось впервые, но это Сайори бежит ко мне размахивая руками."
    "И чего только она пристала ко мне?"
    s '"ХЕЕЕЙЙЙ"'
    "Сайори прибежала ко мне со скоростью три Сайори в секунду."
    show sayori 1p at t11 zorder 1
    with dissolve
    s '"Фуухх, на этот раз я тебя догнала."'
    "А я то надеялся, что это не произойдет."
    show sayori 2a at t11
    with dissolve
    s '"Спасибо, что подождал меня, это очень мило с твоей стороны."'
    mc '"Ага, без проблем."'
    "Господи, за что?"
    "A ведь я надеялся прожить обычный день."
    show sayori 4a  zorder 1
    with dissolve
    s '"Кстати, сегодня ты идешь со мной в мой клуб."'
    show sayori 4a zorder 2
    with dissolve
    mc '"Но я не хочу никуда вступать."'
    "Меня устраивала та жизнь, которая у меня сейчас."
    "Учусь я так-себе, не говоря о насмещках в школе, а из друзей у меня только Сайори. "
    "{i}Сайори...{/i}"
    "Хотя, возможно, меня не совсем все устраивает."
    "Но Сайори запрещает мне думать об этом слишком долго."
    "Она говорит, что мой IQ слишком мал для того чтобы думать над этим."
    "Хотя это не совсем так."
    "Недавно у нас в школе был тест на IQ."
    "Мой результат — 67."
    "Я не знал, много это или мало, поэтому спросил у мамы."
    "Она сказала, что я большой молодец и что это очень большая цифра."
    "Чтобы убедиться, она попросила меня посчитать до неё."
    "И знаете что?"
    "67 — это действительно ОЧЕНЬ большое число."
    "Мне даже пришлось достать калькулятор, чтобы не сбиться."
    "После этого я окончательно убедился, что я довольно умный."
    show sayori 1q at t11 zorder 2
    with dissolve
    s '"Ой, да кому интересно твое мнение."'
    show sayori 4a at t11
    s '"Или ты идёшь со мной, или я снова запру тебя в женском туалете."'
    s '"Как в прошлый раз."'
    show sayori 4r at t11 zorder 3
    with dissolve
    mc '"НЕТ, толко не это."'
    mc '"Хорошо, Сайори, я пойду с тобой в клуб."'
    "В прошлый раз, когда Сайори заперла меня в туалете, всё закончилось очень плохо."
    "Меня заставили сделать презентацию."
    "На тему:"
    "{i}'Почему нельзя подглядывать за девушками в туалете.'{/i}"
    "Хотя я вообще-то просто пытался выбраться."
    "Вдобавок мне пришлось неделю убираться в школьном санузле."
    "Теперь у меня есть прозвище."
    "'Командир санузлов'."
    "Мама сказала, что это отличное прозвище."
    "Потому что командир — это важная должность."
    "Я надеюсь, что когда-нибудь меня повысят до генерала."
    "Тогда мама точно будет мной гордиться."
    "Что касается Сайори..."
    "Она постоянно так надо мной шутит."
    "Но у меня всё равно больше нет друзей."
    "Поэтому я продолжаю с ней дружить."
    "Например, на прошлой неделе она заперла меня в классе."
    "И я просидел там все выходные."
    "В понедельник она сказала, что сделала это, чтобы я не опоздал в школу."
    "..."
    "Наверное, в этом есть смысл."
    "Блин, какая же у меня заботливая подруга."
    "Надеюсь она и дальше будет так обо мне заботиться."
    show sayori 4r at t11 zorder 2
    with dissolve
    s '"Отлично, я зайду к тебе после занятий."'
    mc '"Хорошо."'
    scene bg class_day with wipeleft_scene
    "Уроки прошли как обычно."
    "Не считая того что я еле дошел до школы со своим рюкзаком."
    "По ощущениям он весит тонну."
    "Но это ещё не все."
    "Утром я споткнулся о собственные шнурки, потом, как оказалось, забыл дома свое домашнее заддание по матиматике."
    "И учтель сказал мне свою фирменную фразу 'А голову ты дома не забыл'."
    "Я испугался, но потом проверил и моя голова оказалось на месте."
    "Хорошо, что {i}на этот раз{/i} я не забыл её."
    "Но, в добавок к этому, за обедом я умудрился пролить на себя свой суп."
    "{i}Три раза...{/i}"
    "Но самое главное, что я выжил."
    "Нужно было придумать план как пережить следующий день."
    "Внезапно раздался громкий удар и дверь вылетила со своих петель."
    "А, ну ничего удивительного, это Сайори, как обычно, зашла в мой класс."
    show sayori 1a at t11 zorder 2
    "Сайори подошла ко мне."
    s '"Ну что, готов к унижению? Ой, в смысле, к клубу."'
    "Наверняка Сайори просто оговорилась и мне не стоит обращать на это внимание."
    mc '"Да, но я ещё немного волнуюсь."'
    s '"Не волнуйся, мы не будем тебя сильно унижать."'
    show sayori 5b zorder 2
    s' "{i}По крайней мере сегодня.{/i}"'
    "Последнюю фразу Сайори пробормотала про себя, так что я ничего не услышал."
    mc '"Ладно, пошли."'
    show sayori 2q zorder 2
    s '"Отлично, сейчас начнется веселье."'
    "Ну если там будет весело, то, может, все не так уж и плохо."
    "Тем более, что Сайори пообещала меньше прикалываться надо мной."
    "Может быть она даже перестанет меня бить."
    "Это было бы здорово."
    "Но не успел я договорить, как Сайори взяла меня за ухо и потащила к выходу из класса, паралельно задевая каждую парту на пути."
    "Мне было немного больно, но Сайори сказала, что она таким образом проводит 'краштест' моего тела, и это очень полезно для меня."
    "Блин, какая же Сайори заботливая, я очень надеюсь, что она будет и дальше заботится обо мне."
    scene bg corridor with wipeleft_scene 
    stop music fadeout 2.0
    "И вот я здесь… в месте, куда меня буквально притащили силой. Литературный клуб. Звучит безобидно… что может пойти не так?"
    "Я все ещё нервничаю, но надеюсь, что Сайори поддержит меня."
    "Мы зашли в комнату."
    play sound closet_open
    scene bg club_day with wipeleft_scene
    pause(0.1)
    play music t3
    show sayori 1a at l42 zorder 2 
    s '"Всем привет! Я привела новенького!"'
    mc '"Я… вообще-то сам пришёл… наверное…"'
    show natsuki 1b at t43 zorder 2
    with dissolve
    u '"Чего?! Это он новенький?"'
    show natsuki 4b zorder 2 at f43
    u '"Он выглядит так, будто потерялся по дороге в столовую."'
    mc '"Эй! Я не…"'
    "Я задумался на секунду."
    mc '"…ладно, один раз было."'
    "Сайори подошла и прошептала мне."
    show sayori 2a zorder 2 at f42 
    show natsuki 4b zorder 1 at t43 
    s '"Это Нацуки, не обращай на нее внимание, когда она так себя ведет."'
    show sayori 2a zorder 1 at t42  
    show yuri 1a at t44 zorder 1 
    with dissolve
    u '"О-он выглядит… эм… довольно…доступным для литературного развития."'
    show sayori 2c zorder 2 at f42
    show yuri 1a zorder 1 at t44   
    s '"Юри, ты хотела сказать “лёгкая добыча”?"'
    show sayori 2c zorder 1 at t42
    show yuri 3p zorder 2 at f44
    y '"Я-я такого не говорила! Хотя…"'
    show yuri 4b zorder 2 
    y '"возможно, он действительно… кхм… нуждается в помощи."'
    show yuri 4b zorder 1 at t44
    show natsuki 4w zorder 2 at f43
    n '"Помощи? Да ему инструкция нужна, как дышать!"'
    mc '"Я умею дышать!"'
    n '"Докажи."'
    "{i}Глубокий вдох...{/i}"
    show natsuki 4w zorder 1 at t43
    show sayori 2x zorder 2 at f42
    s '"Ого, он справился! Я горжусь тобой!"'
    show sayori 2x at t41 zorder 1
    show monika 1a at t42 zorder 2
    with dissolve
    m '"О, вы уже познакомились?"'
    show monika 2b zorder 1 at f42
    m  '"Добро пожаловать в литературный клуб! Надеюсь, ты найдёшь здесь… вдохновение."'
    mc '"Спасибо… надеюсь, я хотя бы выживу."'
    "С Моникой я уже был знаком, мы вместе учлись в одном классе."
    "Надеюсь, что она не будет меня осуждать за каждое моё действие."
    show sayori 4a zorder 2  at f41
    show monika 2b zorder 1 at t42
    s '"Не переживай! Если что — мы тебя починим!"'
    show sayori 4a zorder 1 at t41
    show natsuki 1b zorder 2 at f43
    n '"Или сломаем окончательно."'
    show natsuki 1b zorder 1 at t43
    show yuri 2f zorder 2 at f44
    y '"Это… тоже форма развития…"'
    mc '"Я начинаю жалеть, что не остался дома…"'
    show yuri 2f zorder 1 at t44
    show sayori 4a zorder 2 at f41
    s '"Поздно! Теперь ты официально наш!"'
    show sayori 4a zorder 1 at t41
    show monika 2b zorder 2 at f42
    m '"Тогда давайте начнём клубное собрание."'
    show monika 1k zorder 2 
    m '"И, пожалуйста, постарайтесь не сломать новенького в первый же день."'
    show monika 2k zorder 1 at t42
    show natsuki 1w zorder 2 at f43
    n '"Никаких обещаний."'
    "Отлично. Меня окружают четыре девушки, и каждая из них по-своему опасна. Кажется, моя нормальная жизнь официально закончилась."
    show natsuki 1w zorder 1 at t43
    show monika 1a zorder 2 at f42
    m '"Раз уж такое дело, то давайте отпразнуем вступление нового члена кексами и чаем."'
    scene bg club_day with dissolve
    "Девушки сдвинули парты, чтобы получился один большой стол."
    "Меня посадили за стол. Передо мной чай. Я не уверен, как его пить так, чтобы меня не осудили…"
    show sayori 1c at t21 
    with dissolve
    s '"Ну что, это чай. Его не надо бояться!"'
    mc '"Я просто не уверен… есть какие-то правила?"'
    show natsuki 4b at t22
    with dissolve
    n '"Да. Не пролей его на себя, как суп в столовой."'
    mc '"ЭЙ! Откуда ты это знаешь?!"'
    show sayori 2a zorder 2 at f21
    show natsuki 4b zorder 1
    s '"Я веду дневник его позора."'
    mc '"ЧТО?"'
    "Внеапно Нацуки поставила тарелку, накрытою фольгой, на стол."
    show sayori 2a zorder 1 at t21
    show natsuki 1g zorder 2 at f22
    n '"Ладно, забудь про чай. Лучше ешь. Это я сделала."'
    "Я беру кекс в руки и внимательно осматриваю его."
    mc '"Он выглядит… слишком хорошо для меня."'
    show natsuki 4f zorder 2
    n '"Если ты сейчас скажешь, что боишься его есть, я тебя выгоню."'
    mc '"Нет-нет! Я просто… морально готовлюсь."'
    "Я откусываю кекс."
    "Ого. Это… реально вкусно."
    mc '"Вау… это очень вкусно."'
    show natsuki 1s zorder 2
    n '"Ну… я и так знаю."'
    show natsuki 1s zorder 1 at t22
    show sayori 4x zorder 2 at f21
    s '"ОГО! Он не облажался!"'
    mc '"Почему у меня ощущение, что вы ожидали обратного?.."'
    show sayori 4x at t31 zorder 1
    show natsuki 1s at t32 zorder 1
    show yuri 1b at t33 zorder 2
    with dissolve
    y '"Эм… раз уж ты здесь…"'
    show yuri 1b at f33 zorder 2
    y '"М-можно спросить… что ты любишь читать?.."'
    "Отличный вопрос… жаль, что у меня нет отличного ответа."
    mc '"Ну… я… читаю… иногда…"'
    show yuri 1b zorder 1 at t33
    show natsuki 1e zorder 2 at f32
    n '"Это не ответ."'
    show natsuki 1e zorder 1 at t32
    show sayori 1a zorder 2 at f31
    s '"Он читает меню в столовой! Иногда даже правильно!"'
    mc '"ЭЙ!"'
    show sayori 1a zorder 1 at t31
    show yuri 1c zorder 2 at f33
    y '"Э-это… тоже начало…"'
    show sayori 1a at t41 zorder 1
    show natsuki 1a at t43 zorder 1
    show yuri 1c at t44 zorder 1
    show monika 1a at t42 zorder 2
    with dissolve
    m '"Не переживай, у всех есть свой путь в литературе."'
    mc '"Спасибо… кажется…"'
    show monika 1a zorder 1
    show yuri 2m zorder 2 at f44
    y '"М-мне, например, нравятся… более глубокие и атмосферные книги…"'
    show yuri 4b zorder 2
    y '"Сложные сюжеты… психологические темы…"'
    show sayori 2x zorder 2 at f41
    show yuri 4b zorder 1 at t44
    s '"Kороче, книги где ты ничего не понимаешь первые 50 страниц!"'
    show sayori 2x zorder 1 at t41
    show yuri 3p zorder 2 at f44
    y '"С-Сайори!"'
    show yuri 3p zorder 1  at t44
    show natsuki 1m zorder 2 at f43
    n '"Ага, а потом ещё 50 страниц думаешь, зачем вообще начал."'
    show yuri 4b zorder 2 at f44
    show natsuki 1m zorder 1 at t43
    y '"Это… не совсем так…"'
    show yuri 2f zorder 2
    y '"А ты… может быть… хотел бы попробовать что-то подобное?.."'
    mc '"Если там есть… картинки…"'
    show yuri 2f zorder 1 at t44
    show natsuki 5w zorder 2 at f43
    n '"О БОЖЕ."'
    show natsuki 5w zorder 1 at t43
    show sayori 1x zorder 2 at f41
    s '"Не волнуйся! Мы найдём ему книжку с картинками!"'
    show sayori 1x zorder 1 at t41
    show monika 1k zorder 2 at f42
    m '"Думаю, у нас найдётся что-то для каждого уровня."'
    "Отлично. Меня официально записали в клуб… и в категорию ‘начальный уровень с картинками'."
    scene bg club_day with wipeleft_scene
    "Я начал немного расслабляться… возможно, всё не так уж и плохо…"
    "Но внезапно Моника делает небольшой хлопок в ладоши, привлекая внимание."
    show monika 1a at t11 zorder 2
    with dissolve
    m '"Хорошо, все! Раз уж мы познакомились…"'
    "О нет. Когда она так говорит — это не к добру…"
    show monika 2b
    m '"У меня есть отличная идея, чтобы помочь нашему новенькому освоиться!"'
    show sayori 1x at f21 zorder 2
    with dissolve
    show monika 2b at t22 zorder 1
    s '"Ооо, это будет весело!"'
    "Сайори посмотрела на меня с дьявольской улыбкой."
    mc '"Почему мне это уже не нравится?.."'
    show sayori 1x at t31 zorder 1
    show monika 2b at t32 zorder 1
    show natsuki 5w at f33 zorder 2
    n '"Потому что это точно что-то тупое."'
    show monika 2a zorder 2 at f32
    show natsuki 5w zorder 1 at t33
    m '"Давайте все напишем по стихотворению к завтрашнему дню!"'
    mc '"..."'
    mc '"Подожди. Что?"'
    show sayori 4r at h31
    show monika 2a zorder 1 at t32
    s '"СТИХИ!"'
    mc '"Я не умею писать стихи."'
    show sayori 4r zorder 1 
    show natsuki 5e zorder 2 at f33
    n '"Это видно."'
    show sayori 4r at t41 zorder 1
    show monika 2a at t42 zorder 1
    show natsuki 5e at t43 zorder 1
    show yuri 1j at f44 zorder 2
    y '"Н-ничего страшного… это… приходит с практикой…"'
    mc '"А есть вариант… не практиковаться?"'
    show yuri 1j at t44 zorder 1 
    show sayori 4x at f41 zorder 2
    s '"Нет~"'
    show sayori 4x at t41 zorder 1
    show monika 2k at f42 zorder 2
    m '"Не переживай, это просто способ выразить себя."'
    mc '"А если мне нечего выражать?.."'
    show monika 2k zorder 1 at t42
    show natsuki 1e zorder 2 at f43
    n '"Тогда выражай пустоту. Тебе подойдёт."'
    show natsuki 1e zorder 1 at t43
    show sayori 1h at f41 zorder 2 
    s '"О! Он может написать стих про то, как он пытался выпить чай!"'
    mc '"Это была сложная ситуация!"'
    show sayori 1h at t41 zorder 1     
    show yuri 2d at f44 zorder 2
    y '"Э-это… может быть довольно… символично…"'
    mc '"Вы все серьёзно сейчас?.."'
    show yuri 2d at t44 zorder 1
    show monika 1a zorder 2 at f42
    m '"Абсолютно."'
    show monika 5a zorder 2
    m '"Завтра мы все поделимся своими стихами."'
    "Вот и всё. Моя судьба решена. Меня заставят писать стихи… и, скорее всего, осудят за них."
    "Хуже уже и быть не может."
    "Сайори наклоняется ко мне и шепчет."
    show monika 5a zorder 1 at t42
    show sayori 2x at f41 zorder 2
    s '"{i}Не переживай… если что, я помогу!{/i}"'
    mc '"Это меня почему-то пугает ещё больше…"'
    show sayori 2x at t41 zorder 1
    show natsuki 1w zorder 2 at f43
    n '"И правильно."'
    show natsuki 1e zorder 1 at t43
    show yuri 4a at f44 zorder 2
    y '"Я… тоже могу… дать совет… если хочешь…"'
    mc '"Спасибо… думаю, мне понадобится вся возможная помощь…"'
    show yuri 4a at t44 zorder 1
    show monika 2b zorder 2 at f42
    m '"Тогда решено!"'
    m '"Все пишем стихотворения к завтрашнему дню~"'
    scene bg club_day with wipeleft_scene
    "Отлично. Я пришёл сюда попить чай… а ухожу с домашкой. Худшая сделка в моей жизни."
    "Но, надеюсь, что, хотя бы, Сайори сдержит своё обещание, касательно издевательств надо мной."
    "Но как бы то нибыло, нужно заняться стихами."
    "Надеюсь у меня хоть что-то получиться и на меня не будут сильно кричать."
    stop music fadeout 2.0
    scene black with fade
    "На следующий день..."
    scene bg class_day with fade
    pause(0.1)
    play music t2
    "..."
    "Это будет второй день в литературном клубе."
    "Вчера мне задали написать стих."
    "Я пытался."
    "Очень пытался."
    "…примерно три минуты."
    "После этого я понял, что поэзия — не моё."
    "Поэтому я придумал гениальный план."
    "Я написал по 20 случайных слов для каждой девушки."
    "Это же почти как стих… наверное."
    scene bg corridor with wipeleft_scene
    "Надеюсь сегодня будет день получше, чем вчера."
    "Хотя, я , вроде как, понравился девушкам."
    "Особено Нацуки."
    "Кажись, я ей больше всего понравился."
    "Думаю она будет рада меня сегодня видеть."
    "Я захожу в комнату."
    stop music
    play sound closet_open
    scene bg club_day with wipeleft_scene
    pause(0.1)
    play music t3
    "Я пришел самым последним, остальные уже сидели здесь."
    "Услышав звук отравающиеся двери, Сайори подошла ко мне."
    show sayori 1a at t11 zorder 2 
    with dissolve
    s '"О! Ты пришёл!"'
    show sayori 1a at t21 zorder 1
    show monika 1a at t22 zorder 2
    m '"Добро пожаловать обратно!"'
    show sayori 1a at t31 zorder 1
    show monika 1a at t32 zorder 1
    show yuri 1b at t33 zorder 2
    y '"Н-нам… очень интересно увидеть… твой стих…"'
    show sayori 1a at t41 zorder 1
    show monika 1a at t42 zorder 1
    show yuri 1b at t44 zorder 1
    show natsuki 1b at t43 zorder 2
    n '"Подожди."'
    "Нацуки подозрительно смотрт на меня."
    show natsuki 2g zorder 2 at f43
    n '"У меня плохое предчувствие."'
    show natsuki 2g zorder 1 at t43
    show sayori 2x zorder 2 at f41
    s '"А у меня хорошее! Это всегда значит, что будет смешно!"'
    show sayori 2x zorder 1 at t41
    show natsuki 5w zorder 2 at f43
    n '"Моника."'
    show natsuki 5w zorder 1 at t43
    show monika 1b zorder 2 at f42
    m '"Да?"'
    show natsuki 5w zorder 2 at f43
    show monika 1b zorder 1 at t42
    n '"Давай сегодня будем делиться стихами сейчас, а не в конце."'
    show natsuki 5w zorder 1 at t43
    show monika 1d zorder 2 at f42
    m '"Хм? Почему?"'
    show natsuki 1e zorder 2 at f43
    show monika 1d zorder 1 at t42
    n '"Потому что если он будет читать стих последним…"'
    show natsuki 5e zorder 2
    n '"мы можем застрять тут до ночи."'
    mc '"Эй!"'
    show natsuki 5e zorder 1 at t43
    show yuri 1i zorder 2 at f44
    y '"Э-это… правда может занять… некоторое время…"'
    mc '"Почему вы все так уверены, что всё будет плохо?!"'
    show natsuki 4n zorder 2 at f43
    show yuri 1i zorder 1 at t44
    n '"Потому что я смотрю на тебя."'
    show natsuki 4n zorder 1 at t43
    show monika 1l zorder 2 at f42
    m '"Ну… раз уж все так заинтригованы…"'
    show monika 1j zorder 2
    m '"Тогда давайте начнём прямо сейчас."'
    show monika 1j zorder 1 at t42
    show sayori 2j zorder 2 at f41
    s '"Ты же написал стих… правда?"'
    mc '"Конечно."'
    s '"Почему ты сказал это так, будто врёшь?"'
    mc '"Я не вру!"'
    "Технически… я не вру."
    "Это… просто не совсем стих."
    show sayori 2j zorder 1 at t41
    show natsuki 4i zorder 2 at f43
    n '"Ладно, давай уже показывай."'
    mc '"Хорошо… только не судите строго."'
    n '"Уже боюсь."'
    show natsuki 4i zorder 1 at t43
    show yuri 2i zorder 2 at f44
    y '"Я… тоже немного…"'
    show yuri 2i zorder 1 at t44
    show sayori 4r zorder 2 at f41
    s '"Я готова смеяться!"'
    show sayori 4r zorder 1 at t41
    show monika 2b zorder 2 at f42
    m '"Тогда начинаем~"'
    scene bg club_day with wipeleft_scene
    "Отлично."
    "Сейчас они узнают, что такое… поэзия нового поколения."
    "…список из 20 случайных слов."
    stop music
    scene bg club_day with wipeleft_scene
    pause(0.1)
    play music t5
    label poem_sharing:

    $ sayori_done = False
    $ natsuki_done = False
    $ yuri_done = False
    $ monika_done = False
    $ poems_shared = 0

    jump poem_menu

label poem_menu:

    if poems_shared == 0:
        "Кто будет первый читать моё недорозумение?"

    elif poems_shared == 1:
        "Интересно, кто будет страдать следующим..."

    elif poems_shared == 2:
        "Будут ли на меня кричать в этот раз?"

    elif poems_shared == 3:
        "Осталось пережить ещё один раз..."

    menu:

        "Сайори" if not sayori_done:
            $ sayori_done = True
            $ poems_shared += 1
            jump poem_sayori

        "Нацуки" if not natsuki_done:
            $ natsuki_done = True
            $ poems_shared += 1
            jump poem_natsuki

        "Юри" if not yuri_done:
            $ yuri_done = True
            $ poems_shared += 1
            jump poem_yuri

        "Моника" if not monika_done:
            $ monika_done = True
            $ poems_shared += 1
            jump poem_monika


label poem_sayori:
    show sayori 1x at t11 zorder 2
    with dissolve
    s '"О! Давай посмотрим!"'
    s '"Солнце…"'
    s '"Радость…"'
    show sayori 2n zorder 2
    s '"…депрессия?"'
    mc '..."'
    show sayori 2s zorder 2
    s '"ВАУ!"'
    mc '"Почему “вау”?!"'
    show sayori 4s zorder 2
    s '"Это лучшее, что ты написал за всю жизнь!"'
    mc '"Это буквально первый стих в моей жизни."'
    show sayori 2x zorder 2
    s '"Значит ты сразу начал с шедевра!"'
    s '"Мне особенно нравятся “солнце” и “радость”!"'
    show sayori 4q zorder 2
    s '"Они такие тёплые!"'
    show sayori 2x zorder 2
    s '"А “депрессия”…"'
    mc '"Это случайно."'
    s '"Это очень глубокая метафора!"'
    s '"Иногда жизнь — это солнце…"'
    s '"иногда радость…"'
    show sayori 1y zorder 2
    s '"а иногда ты просто лежишь и не хочешь вставать."'
    mc '"Это звучит слишком реально."'
    show sayori 2a zorder 2
    s '"Ладно! Теперь мой стих!"'
    call showpoem(poem_st1)
    show sayori 2x zorder 2
    s '"Ну как? Правда мило?"'
    mc '"Да… он очень… энергичный."'
    s '"Я старалась!"'
    s '"Но твой стих всё равно мой любимый."'
    mc '"Там просто список слов."'
    show sayori 1d zorder 2
    s '"Это креативный список слов!"'
    mc '"Я рад, что хотя бы тебе понравилось."'
    show sayori 2c zorder 2
    s '"Конечно понравилось!"'
    show sayori 1q zorder 2
    s '"Если честно… я просто рада, что ты вообще написал что-то."'
    mc '"Это звучит как очень низкие ожидания."'
    show sayori 1x zorder 2
    s '"Ну… это ты."'
    mc '"Спасибо за поддержку."'
    s '"Ладно! Пойди покажи стих остальным!"'
    s '"Я хочу увидеть их лица!"'
    hide sayori
    with dissolve
    jump poem_after

label poem_natsuki:
    show natsuki 1m at t11 zorder 2
    with dissolve
    n '"Хмф... Ладно, давай сюда."'
    show natsuki 1s zorder 2
    n '"Хм…"'
    n '"Кекс…"'
    n '"Милый…"'
    show natsuki 1v at hop
    n '"…папа."'
    mc '"Я чувствую, что сейчас будет крик."'
    n '"ЧТО ЭТО ТАКОЕ?"'
    mc '"Поэзия."'
    show natsuki 5p zorder 2
    n '"Это не поэзия, это список покупок психа."'
    mc '"Но там есть твои слова!"'
    show natsuki 1q zorder 2
    n '"Да, “кекс” и “милый” нормальные!"'
    show natsuki 1o zorder 2
    n '"Но, с чего ты решил написать “папа” в стихе про кексы?!"'
    mc '"Я писал случайные слова!"'
    show natsuki 5n zorder 2
    n '"Это видно!"'
    n '"“Кекс” и “милый” нормальные!"'
    show natsuki 2r zorder 2
    n '"Но “папа” тут вообще откуда?!"'
    mc '"Я паниковал."'
    show natsuki 1v zorder 2
    n '"Ты паниковал… и первым делом написал “папа”?"'
    mc '"Теперь когда ты так говоришь — это звучит странно."'
    show natsuki 3s zorder 2
    n '"Ладно…"'
    n '"Хотя бы кекс ты написал правильно."'
    mc '"Это был самый лёгкий момент моего творчества."'
    show natsuki 1c zorder 2
    n '"Ладно, вот мой стих."'
    call showpoem(poem_nt1)
    show natsuki 1e zorder 2
    n '"Ну?"'
    mc '"Он милый."'
    show natsuki 4f zorder 2
    n '"Что ты щас сказал?"'
    mc '"Он намного лучше моего."'
    show natsuki 5w zorder 2
    n '"Это не сложно."'
    mc '"Эй."'
    show natsuki 2h zorder 2
    n '"Я всё ещё не понимаю, как ты написал “кекс”, “милый”… и “папа” в одном стихе."'
    mc '"Это был творческий кризис."'
    show natsuki 5i zorder 2
    n '"Это был мозговой кризис."'
    mc '"Это грубо."'
    show natsuki 5z zorder 2
    n '"Но честно."'
    show natsuki 1a zorder 2
    n '"Ладно… иди уже покажи его другим."'
    mc '"Почему у меня ощущение, что ты хочешь посмотреть, как они страдают?"'
    n '"Потому что хочу."'
    hide natsuki
    with dissolve
    jump poem_after

label poem_yuri:
    show yuri 4a at t11 zorder 2
    with dissolve
    y '"М-можно посмотреть…?"'
    mc '"Конечено."'
    "Я передал Юри свой стих."
    show yuri 2g zorder 2
    y '"Тьма…"'
    y '"Бездна…"'
    show yuri 3y6 zorder 2 
    y '"…самоубийство…"'
    mc '"..."'
    mc '"Я не специально!"'
    y '"Это… очень сильные слова…"'
    y '"“Тьма” и “бездна” создают… глубокую атмосферу…"'
    show yuri 3y4 zorder 2
    $ style.say_dialogue = style.edited2
    y '{i}"A “самоубийство”…"{/i}'
    $ style.say_dialogue = style.normal
    show yuri 3y5 zorder 2
    mc '"Я просто писал слова наугад."'
    show yuri 2m zorder 2
    y '"Иногда… случайность раскрывает… скрытые мысли человека."'
    mc '"Это звучит немного пугающе."'
    show yuri 3p zorder 2
    y '"П-прости! Я не хотела!"'
    show yuri 4c zorder 2
    y '"Возьми, наверное, мой стих."'
    y '"А потом..."'
    show yuri 4b zorder 2
    y '"Мы можем его обсудить."'
    "Юри дала мне свой стих."
    call showpoem(poem_yt1)
    show yuri 4a zorder 2
    y '"Т-тебе… понравилось?"'
    mc '"Да… правда."'
    mc '"Он очень… глубокий."'
    "Стих Юри слишком умный для меня."
    show yuri 2u zorder 2
    y '"Спасибо…"'
    show yuri 2f zorder 2
    y '"Я всё ещё думаю о твоих словах…"'
    y '"Тьма"'
    y '"Бездна"'
    show yuri 2l zorder 2
    y '"…и “самоубийство”."'
    mc '"Я правда не хотел делать его таким мрачным."'
    show yuri 2m zorder 2
    y '"Иногда… мрачные мысли тоже могут быть красивыми…"'
    show yuri 3n zorder 2
    y '"П-прости! Я опять странно говорю!"'
    mc '"Нет, всё нормально…"'
    mc '"Просто немного… пугающе."'
    show yuri 2d zorder 2
    y '"Я… постараюсь быть менее пугающей…"'
    y '"Пожалуйста покажи стих остальным тоже…"'
    hide yuri
    with dissolve
    jump poem_after

label poem_monika:
    show monika 1a at t11 zorder 2
    with dissolve
    m '"Хорошо! Давай посмотрим твой стих."'
    m '"Музыка…"'
    m '"Улыбка…"'
    show monika 1g zorder 2
    m '"…подвешенный."'
    show monika 1o zorder 2
    m '"Хм."'
    mc '"Насколько всё плохо?"'
    show monika 2l zorder 2
    m '"Честно? Возможно… всё не так уж и плохо."'
    mc '"Правда?"'
    show monika 3b zorder 2
    m '"“Музыка” и “улыбка” — отличные слова."'
    show monika 1m zorder 2
    m '"А “подвешенный”…"'
    mc '"Я не знаю почему я это написал."'
    show monika 1n zorder 2
    m '"Ну… иногда персонажи в играх…"'
    show monika 5a zorder 2
    m '"{i}…немного зависают.{/i}"'
    mc '"Это звучит как баг."'
    show monika 1m zorder 2
    m '"Возможно. Но не волнуйся — у нас в клубе никто не..."'
    show monika 5a zorder 2
    m '"{i}...зависает.{/i}"'
    show monika 1a zorder 2
    m '"Ладно, теперь моя очередь делиться стихом."'
    "Моника передала мне её стих."
    call showpoem(poem_mt1)
    m '"Ну что думаешь?"'
    mc '"Он… очень умный."'
    show monika 1d zorder 2
    m '"Это хороший способ сказать, что ты его не понял?"'
    mc '"Немного."'
    show monika 2b zorder 2
    m '"Ничего страшного."'
    m '"Поэзия иногда работает именно так."'
    m '"Но твой стих мне всё равно понравился."'
    mc '"Даже со словом “подвешенный”?"'
    show monika 1m zorder 2
    m '"Конечно."'
    m '"Иногда персонажи просто… немного..."'
    show monika 5a zorder 2
    m '"{i}зависают.{/i}"'
    mc '"Я начинаю подозревать, что это шутка, которую я не понимаю."'
    show monika 1l zorder 2
    m '"Возможно~"'
    show monika 2b zorder 2
    m '"В любом случае, думаю остальные уже ждут тебя."'
    mc '"Да… пора завершить мой литературный тур позора."'
    hide monika
    with dissolve
    jump poem_after


label poem_after:

    if poems_shared == 4:
        jump after_poems
    scene bg club_day with wipeleft_scene
    jump poem_menu


label after_poems:
    stop music
    scene bg club_day with wipeleft_scene
    pause(0.1)
    play music t3
    "Итак… я пережил это."
    "Я показал свой ‘стих’ всем в клубе…"
    "…и каким-то чудом меня ещё не выгнали."
    "Честно говоря, это уже победа."
    "Я осмотрелся по комнате."
    "Сайори выглядит так, будто всё ещё думает о моём ‘шедевре’."
    "Моника спокойно просматривает стихи, как будто ничего странного не произошло."
    "…а вот Юри и Нацуки…"
    "…кажется, они как раз делятся стихами друг с другом."
    show natsuki 2s at f21 zorder 2
    show yuri 2i at t22 zorder 1
    n '"Эм… это…"'
    show natsuki 2i at f21 zorder 2
    n '"…очень длинно."'
    show natsuki 2i zorder 1 at t21
    show yuri 2i zorder 2 at f22
    y '"А твой… очень… короткий."'
    stop music
    play music t7
    show natsuki 2e zorder 2 at f21
    show yuri 2i zorder 1 at t22
    n '"Потому что я умею писать нормально, а не как учебник по философии!"'
    show natsuki 2e zorder 1 at t21
    show yuri 2k zorder 2 at f22
    y '"Это называется описание атмосферы…"'
    show natsuki 2e zorder 2 at f21
    show yuri 2k zorder 1 at t22
    n '"Это называется “слишком много слов”."'
    show natsuki 2e zorder 1 at t21
    show yuri 2m zorder 2 at f22
    y '"Иногда… простота может быть… поверхностной."'
    show natsuki 1o zorder 2 at f21
    show yuri 2m zorder 1 at t22
    n '"Ты только что назвала мой стих поверхностным?!"'
    show natsuki 1o zorder 1 at t21
    show yuri 3n zorder 2 at f22
    y '"Я… не это имела в виду…"'
    show natsuki 1e zorder 2 at f21
    show yuri 3n zorder 1 at t22
    n '"Нет, именно это!"'
    show natsuki 1e zorder 1 at t21
    show yuri 3o zorder 2 at f22
    y '"Я просто считаю… что поэзия может быть глубже…"'
    show natsuki 1e zorder 2 at f21
    show yuri 3o zorder 1 at t22
    n '"А я считаю, что она не должна звучать как скучная лекция!"'
    "О нет."
    "Я узнаю этот момент."
    "Это тот момент, когда разговор превращается в спор."
    show natsuki 1e zorder 1 at t21
    show yuri 1r zorder 2 at f22
    y '"По крайней мере мои стихи пытаются сказать что-то серьёзное."'
    show natsuki 2o zorder 2 at f21
    show yuri 1r zorder 1 at t22
    n '"А мои хотя бы интересно читать!"'
    "Кажется, они очень разозлились."
    "Может стоит что-то сделать?"
    show natsuki 2o zorder 1 at f21
    show yuri 1r zorder 2 at t22
    n '"По крайней мере я не использую слова из-за которых у [player] начинается сердечный притуп."'
    show natsuki 2o zorder 1 at t21
    show yuri 1r zorder 2 at f22
    y '"Ну в моих, по крайней мере, показывается, что у меня есть хоть какой-то ителект!"'
    "Ладно."
    "Кажется, я должен что-то сделать."
    "Я же новенький, но… может быть я смогу остановить спор."
    stop music fadeout 5.0
    mc '"Эм… а вы спорите… из-за стиля написания, да?"'
    show natsuki 2g zorder 1 at t21
    show yuri 2f zorder 1 at t22
    "Они молча кивают мне."
    mc '"А давайте я научу вас писать стихи… в моём стиле!"'
    show natsuki 1p at h21
    show yuri 3p at h22
    mc '"Тогда никто не будет спорить."'
    play music t7
    show natsuki 1v at h21
    show yuri 3p zorder 1 
    n '"Ты серьёзно думаешь, что я буду писать как ты?"'
    mc '"Ну… да! Это весело!"'
    mc '"И Сайори уже пробовала, ей понравилось!"'
    show natsuki 1v zorder 1
    show yuri 1n zorder 2 at f22
    y '"Я… э-э… но… это… н-не имеет смысла…"'
    show natsuki 5p zorder 2 at f21
    show yuri 1n zorder 1 at t22
    n '"Весело?! Ты предлагаешь, чтобы мы перестали думать своей головой и просто вставляли случайные слова?!"'
    mc '"Именно!"'
    mc '"Вот видите, никакого спора больше не будет."'
    show natsuki 5p zorder 1 at t21
    show yuri 1o zorder 2 at f22
    y '"…Но… это же… абсурдно…"'
    mc '"Абсурдно? Отлично!"'
    mc '"Абсурдность — это новое направление поэзии!"'
    show natsuki 2w zorder 2 at f21
    show yuri 1o zorder 1 at t22
    n '"Ты совсем с ума сошёл!"'
    show natsuki 2g zorder 1 at t21
    mc '"С ума? Нет!"'
    mc '"Я просто открыл секрет: если вставлять случайные слова, никто не спорит, потому что все шокированы!"'
    "Где-то вдали комнаты послышался крик Сайори."
    s '"Ха-ха! Точно!"'
    show yuri 2h zorder 2 at f22
    y '"Я… я даже не знаю, что сказать…"'
    y '"Это выглядит… как… литературное преступление!"'
    show natsuki 2e zorder 2 at f21
    show yuri 2h zorder 1 at t22
    n '"Литературное преступление?! Я согласна!"'
    show natsuki 5q zorder 2
    n '"…Я просто не понимаю, как это должно работать!"'
    mc '"Очень просто!"'
    mc '"Вы берёте мои 20 слов, вставляете их в стих — и всё!"'
    mc '"Никто больше не спорит."'
    stop music fadeout 2.0
    show natsuki 5i zorder 2
    n '"Ладно… знаешь что, Юри?"'
    play music t8
    show natsuki 1k zorder 2
    n '"У тебя… оказывается, очень классный стиль."'
    n '"Я готова слушать твои стихи хоть всю жизнь…"'
    show natsuki 1s zorder 2
    n '"Лишь бы не писать эти твои 20 слов!"'
    show natsuki 1s zorder 1 at t21
    show yuri 1o zorder 2 at f22
    y '"…Э-э… да, я… я согласна…"'
    show yuri 2l zorder 2 
    y '"Твой стиль… тоже хорош… и я тоже не хочу эти 20 слов…"'
    show natsuki 4b zorder 2 at f21
    show yuri 1a zorder 1 at t22
    n '"Отлично."'
    n '"Значит, спор окончен."'
    mc '"…Окей…"'
    mc '"Значит, я просто гениальный посредник?"'
    s '"Ха-ха! Да! Ты спас спор и даже не понял, как!"'
    "Где-то рядом послышался голос Моники."
    m '"Ну… это действительно сработало."'
    m '"Хотя… всё ещё немного нелепо."'
    hide natsuki
    hide yuri
    with dissolve
    "Отлично."
    "Я вмешался в спор и, благодаря моему невероятному предложению…"
    "…Юри и Нацуки наконец-то согласились."
    "…И, по моему мнению, это подтверждает, что мой стиль 20 случайных слов — абсолютная гениальность."
    "…Моя гениальность не знает границ."
    show monika 1a at t11 
    m '"Ну что ж…"'
    m '"Похоже, всё снова стало немного спокойнее."'
    show monika 5a
    m '"Скажите честно… вам понравилось делиться стихами сегодня?"'
    show monika 5a at t22
    show sayori 1x at t21
    s '"Да! Это было очень весело!"'
    hide sayori
    show natsuki 1s at t21
    n '"Ну…"'
    n '"Это было… терпимо."'
    show natsuki 5n 
    n '"Но некоторые стихи были странные."'
    hide natsuki
    show yuri 1b at t21
    y '"Я… думаю, это был интересный опыт…"'
    y '"Узнать, как разные люди пишут стихи."'
    hide yuri
    with dissolve
    mc '"Эм… да, было… весело."'
    show monika 2b at t11
    m '"Тогда отлично!"'
    m '"В таком случае…"'
    m '"давайте сделаем это ещё раз завтра."'
    m '"Напишите ещё одно стихотворение и принесите его на следующее собрание."'
    m '"Думаю, всем будет интересно увидеть, что у вас получится."'
    show monika 2b at t22
    show sayori 1x at t21
    s '"О! Я уже хочу начать!"'
    hide sayori
    show natsuki 1s at t21
    n '"Хмф… ладно."'
    hide natsuki
    show yuri 1b at t21
    y '"Я постараюсь написать что-нибудь… достойное."'
    hide yuri
    with dissolve
    hide monika
    with dissolve
    "После завершения собрания мы с Сайори отправились домой."
    "Нацуки и Юри вышли первыми, мы были за ними."
    scene bg residential_day with wipeleft_scene
    "Отлично."
    "Я пережил свой очередной день в литературном клубе."
    "Я написал стих… из 20 слов."
    "…и каким-то образом он даже понравился."
    "Более того…"
    "Я ещё и остановил спор между Юри и Нацуки."
    "Честно говоря… я сегодня большой молодец."
    "Завтра я снова напишу стих."
    "И на этот раз он будет ещё лучше."
    "Может быть… даже 20 очень случайных слов."
    "…Но это и есть мой стиль."
    "Я уверен, что завтра все будут в шоке от моего нового шедевра."
    "И тогда они точно оценят мои литературные старания."
    "…Потому что такой гений, как я, не может оставаться незамеченным."
    stop music fadeout 2.0
    scene black with fade
    "На следующий день..."
    scene bg club_day2 with fade
    pause(0.1)
    play music t2
    "Я вхожу в клуб и, сразу же, вижу как Сайори несется ко мне через весь класс."
    show sayori 1x at t11
    s '"О! Ты пришёл!"'
    s '"Отлично!"'
    s '"Слушай… у меня есть маленькая просьба."'
    mc '"Уже боюсь."'
    s '"Ты ведь сегодня проходил мимо магазина, да?"'
    mc '"…Возможно."'
    show sayori 5a
    s '"Значит ты мог бы купить мне печенье!"'
    mc '"Нет."'
    show sayori 3h
    s '"Что?! Почему?!"'
    mc '"Я не могу."'
    s '"Но ты даже не подумал!"'
    mc '"Я подумал."'
    mc '"И решил, что не могу."'
    "Сайори смотрит на меня несколько секунд, потом вдруг щёлкает пальцами."
    show sayori 3n
    s '"Подожди…"'
    show sayori 5b
    s '"У тебя ведь… почти никогда нет денег с собой, да?"'
    mc '"..."'
    show sayori 2c
    s '"Я вспомнила!"'
    s '"В прошлый раз ты хотел купить сок и начал проверять все карманы пять минут!"'
    mc '"Я просто проверял тщательно."'
    s '"А потом сказал, что у тебя есть только…"'
    show sayori 4s at h11
    s '"пуговица, старый автобусный билет и один винтик."'
    mc '"Это был хороший винтик."'
    show sayori 4l 
    s '"Так вот почему ты не купил печенье!"'
    show sayori 1h
    s '"Тебе родители опять не дали денег?"'
    mc '"Они говорят, что если давать мне деньги…"'
    mc '"…то я покупаю очень странные вещи."'
    s '"Например?"'
    mc '"Ну…"'
    mc '"один раз я купил магнит в форме кекса."'
    mc '"потом мини-блокнот “для гениальных идей”, который я так и не открыл."'
    mc '"и книгу «1000 случайных слов для написания стихов»."'
    s '"…"'
    show sayori 1o
    s '"Подожди."'
    show sayori 3c
    s '"Так вот откуда твои 20 слов?!"'
    mc '"Возможно."'
    show sayori 3c at t32
    show yuri 2c at t33
    with dissolve
    y '"Хи-хи..."'
    "Я заметил Юри, которая тихонько смеялась за своей кникой."
    "О нет! Она подслушивала все это время?"
    "Интересно, догадалась ли она, что у меня нет денег?"
    "Юри заметила, что мы смотрим на неё."
    show yuri 2n zorder 2 at f33
    y '"Я… э-э…"'
    show yuri 1o zorder 2
    y '"Я вовсе не подслушивала!"'
    y '"Я просто… стояла здесь…"'
    y '"и… читала."'
    n '"Ага."'
    n '"Очень “случайно” читала рядом с разговором."'
    show natsuki 1i at t31
    with dissolve
    show yuri 4c
    y '"Я правда не подслушивала!"'
    show yuri 4c zorder 1 at t33
    show natsuki 1k zorder 2 at f31
    n '"Хотя я вообще не удивлена."'
    show natsuki 5k zorder 2
    n '"Если честно, я даже понимаю, почему тебе не дают деньги."'
    mc '"Эй."'
    show natsuki 5e zorder 2
    n '"Ты только что признался, что покупаешь книгу случайных слов для стихов."'
    mc '"Это была стратегическая покупка."'
    show natsuki 5g zorder 2
    n '"Ладно. На."'
    "Нацуки кидает Сайори печенье."
    show natsuki 5g zorder 1 at t31
    show sayori 1n zorder 2 at f32
    s '"О-о-о!!"'
    show sayori 4r at h32
    s '"Печенье!!"'
    s '"Нацуки, ты лучшая!"'
    show yuri 2d zorder 1 
    "Сайори радосно ест своё печенье."
    show sayori 4r zorder 1 at t32
    show natsuki 2l zorder 2 at f31
    n '"Не радуйся слишком сильно."'
    n '"Я просто не хочу смотреть на то, как ты выпрашиваешь еду у человека, у которого в кармане…"'
    show natsuki 4z zorder 2
    n '"винтики и пуговицы."'
    "Отлично."
    "Первое, что произошло в клубе сегодня — меня публично разоблачили как человека без денег."
    "…и теперь все знают, что мой поэтический стиль появился благодаря книге «1000 случайных слов для написания стихов»."
    "Замечательное начало дня."
    "Мы ещё пообщались некотрое время, но , внезапно, Моника заходит, слегка запыхавшаяся."
    show sayori 4r at t41
    show yuri 2d at t44
    show natsuki 4a at t43
    show monika 1d at t42
    with dissolve
    m '"Привет всем, извините, что опоздала."'
    mc '"О… Моника! Ты пришла!"'
    show sayori 1c zorder 2 at f41
    s '"Привет! Почему ты опоздала?"'
    show sayori 1c zorder 1 at t41
    show monika 1g zorder 2 at f42
    m '"Эм… простите, я… практиковалась на пианино и так увлеклась, что не услышала звонок."'
    show monika 1g zorder 1 at t42
    show yuri 2m zorder 2 at f44
    y '"Вау, Моника, помимо клуба ты ещё играешь на пианино."'
    y '"Это очень впечатляет."'
    show monika 1l zorder 2 at f42
    show yuri 2m zorder 1 at t44
    m '"Не строй больших ожиданий, это игрой сложно назвать."'
    show monika 2a zorder 2
    m '"Но, я обещаю, что, как только, научусь немного лучше играть, то обязательно вам что-то сыграю."'
    show monika 2a zorder 1 at t42
    show sayori 4x zorder 2 at f41
    s '"Мы все будем ждать, Моника, не спеши с этим."'
    show sayori 4x zorder 1 at t41
    show natsuki 2s zorder 2 at f43
    n '"Хм… интересно."'
    show natsuki 2h zorder 2
    n '"[player], ты хотя бы знаешь, что такое пианино?"'
    mc '"Конечно!"'
    mc '"Пианино — это такая деревянная штука со струнами."'
    mc '"На ней дергаешь струны, и получается музыка."'
    mc '"Эм… хотя подождите…"'
    mc '"Деревянная штука со струнами — это флейта!"'
    mc '"А пианино — это труба, в которую нужно дуть!"'
    show natsuki 4p at d43
    show sayori 1l at d41
    show yuri 2q at d44
    show monika 1m at d42
    s '"…Эм… почти верно."'
    show sayori 1l zorder 1 at t41
    show yuri 2f zorder 2 at f44
    y '"…То есть теперь ты представляешь пианино как трубу, а флейту — как деревянную штуку со струнами?!"'
    mc '"Ну… музыка сложная штука."'
    mc '"Подождите… а если пианино не труба… тогда куда в него дуть?"'
    show yuri 1w zorder 2
    y '"В… в него не нужно дуть…"'
    mc '"Ладно… тогда другой вопрос."'
    mc '"Eсли на пианино нельзя дуть и нельзя дергать струны… тогда как оно вообще работает?!"'
    show yuri 1w zorder 1 at t44
    show sayori 4r zorder 2 at f41
    s '"Ха-ха! [player], ты сейчас реально пытаешься понять музыку?"'
    show yuri 1o zorder 2 at f44
    show sayori 4r zorder 1 at t41
    y '"Я… я даже не знаю, как это объяснить…"'
    mc '"Хорошо… тогда скажите честно…"'
    mc '"пианино вообще существует или вы меня разыгрываете?"'
    show yuri 1n zorder 1 at t44
    show natsuki 1v at h43
    n '"[player]!!! ЗАМОЛЧИ!!! Я БОЛЬШЕ НЕ ВЫДЕРЖУ ЭТОГО БЕЗУМИЯ!!!"'
    show monika 2l zorder 2 at f42
    m '"Ха-ха! Ну что ж… Вчера мы немного затянули со стихами, поэтому сегодня будем делиться ими раньше обычного."'
    mc '"Эм… раньше?"'
    show monika 2l zorder 1 at t42
    show sayori 1x zorder 2 at f41
    s '"Да! Значит, мы можем читать твои 20 случайных слов прямо сейчас, [player]!"'
    mc '"…Окей…"'
    show monika 4b zorder 2 at f42
    show sayori 1x zorder 1 at t41
    m '"Отлично! Тогда начнем сразу, чтобы день был продуктивным."'
    show monika 4b zorder 1 at t42
    show natsuki 5b zorder 2 at f43
    n '"Хм… продуктивным? С этим парнем?"'
    mc '"Э-э… я очень продуктивный!"'
    show natsuki 5b zorder 1 at t43
    show sayori 4x zorder 2 at f41
    s '"Да-да, [player], сегодня мы точно будем смеяться!"'
    hide sayori
    hide natsuki
    hide yuri 
    hide monika
    with dissolve
    "Все пошли к своим партам доставать стихи и я последовал их примеру."
    "На этот раз я хотел всех очень сильно удивить своим произведением."
    "Нет, я не пытался поменять стиль, я попытался сделать нечто больше."
    "Вместо привычных 20 слов, я старался написать 21 ослово."
    "И я пытался, правда пытался."
    "На этот раз целых 4 минуты."
    "Но, к сожалению, у меня не вышло, поэтому я написал 20 слов для каждой девушки, как я делал до этого."
    "Не представляю что бы я делел без книги «1000 случайных слов для написания стихов»."
    "Это, действительно, было лучшее вложение."
    "Пойду, наконец-то, покажу всем своё творение."
    stop music fadeout 2.0
    scene bg club_day with wipeleft_scene
    pause(0.1)
    play music t5
label poem_sharing2:

    $ sayori2_done = False
    $ natsuki2_done = False
    $ yuri2_done = False
    $ monika2_done = False
    $ poems2_shared = 0

    jump poem_menu2

label poem_menu2:
    if poems2_shared == 0:
        "Кому первому посчастливится увидеть мой шедер."
    elif poems2_shared == 1:
        "Кто следующим сможет лицезреть моё чудо-творение."
    elif poems2_shared == 2:
        "Ну что ж... кому повезёт увидеть это произведение искуства."
    elif poems2_shared == 3:
         "Сейчас я точно шокирую своим произведением."
    menu:

        "Сайори" if not sayori2_done:
            $ sayori2_done = True
            $ poems2_shared += 1
            jump poem2_sayori

        "Нацуки" if not natsuki2_done:
            $ natsuki2_done = True
            $ poems2_shared += 1
            jump poem2_natsuki

        "Юри" if not yuri2_done:
            $ yuri2_done = True
            $ poems2_shared += 1
            jump poem2_yuri

        "Моника" if not monika2_done:
            $ monika2_done = True
            $ poems2_shared += 1
            jump poem2_monika


label poem2_sayori:
    show sayori 1a at t11 zorder 2
    with dissolve
    s '"О! [player], давай сначала я прочитаю твой стих!"'
    show sayori 2k
    s '"Хм…"'
    show sayori 2a
    s '"Знаешь, мне это нравится больше, чем вчера!"'
    mc '"Серьёзно?"'
    show sayori 2l
    s '"Да! Он всё ещё немного странный…"'
    show sayori 2a
    s '"Но в этот раз слова как будто… веселее!"'
    mc '"Ну… я старался."'
    mc '"Кстати, я даже пытался написать 21 слово вместо 20."'
    show sayori 1o
    s '"Правда?!"'
    mc '"Да… но у меня не получилось."'
    mc '"Я пересчитывал три раза, и каждый раз всё равно выходило 20."'
    show sayori 4s
    s '"Ха-ха!"'
    show sayori 3x
    s '"Я горжусь тобой, [player]!"'
    s '"Ты правда стараешься!"'
    "Отлично. План сработал."
    "Даже если я не написал 21 слово…"
    "Сайори всё равно считает это достижением."
    s '"Ладно! Теперь мой!"'
    call showpoem(poem_st2)
    mc '"О…"'
    mc '"Этот стих звучит очень… Сайористо."'
    show sayori 3o
    s '"Э?!"'
    mc '"Ну… он милый, немного странный…"'
    mc '"И почему-то заставляет улыбаться."'
    show sayori 3q
    s '"Хи-хи! Спасибо!"'
    "Иногда я думаю, что Сайори может написать стих буквально из двух слов…"
    "И всё равно он будет работать."
    show sayori 1x
    s '"Ладно, иди покажи свой шедевр остальным."'
    show sayori 1r
    s '"Надеюсь, ты обрадуешь их также как меня."'
    hide sayori
    with dissolve
    jump poem_after2


label poem2_natsuki:
    show natsuki 5h at t11 zorder 2
    with dissolve
    n '"Давай уже его сюда."'
    show natsuki 2s 
    n '"Хм."'
    show natsuki 2n
    n '"Ну… ничего другого от тебя я и не ожидала."'
    mc '"Это комплимент?"'
    n '"Нет."'
    n '"Но и не совсем оскорбление."'
    mc '"Кстати, я пытался написать 21 слово."'
    show natsuki 4c
    n '"…что?"'
    mc '"Но не получилось."'
    show natsuki 5y
    n '"Ого."'
    n '"Не слишком ли сильно ты стараешься?"'
    n '"Написать ещё одно слово… это же огромный труд!"'
    mc '"Эй, между прочим это серьёзная поэтическая задача."'
    show natsuki 2l
    n '"Никто не сомневается, что для тебя это сложно."'
    n '"Ладно, держи мой стих."'
    call showpoem(poem_nt2)
    mc '"Хм…"'
    mc '"Стих неплохой."'
    mc '"Но как будто я сегодня старался больше."'
    show natsuki 1p
    n '"ЧТО?!"'
    mc '"Ну… я хотя бы пытался написать 21 слово."'
    show natsuki 1v at h11
    n '"Ты сейчас серьёзно сравниваешь это с настоящим стихом?!"'
    mc '"Я просто стараюсь не обращать внимания на {i}мелочи{/i}."'
    show natsuki 2s 
    n '"…"'
    n '"…"'
    show natsuki 2h
    n '"…"'
    show natsuki 1v at h11
    n '"ТЫ СЕЙЧАС НАЗВАЛ МЕНЯ МЕЛОЧЬЮ?!"'
    mc '"Нет! Я имел в виду… поэтические мелочи!"'
    show natsuki 4o
    n '"Ещё раз скажешь что-то подобное и ты вылетишь отсюда."'
    mc '"Прости, Нацуки, это вообще не то, что я хотел сказать."'
    show natsuki 4q
    n '"Ладно."'
    n '"Иногда мне кажется, что ты специально пытаешься меня разозлить!"'
    mc '"Нет, вовсе, нет."'
    show natsuki 4m
    n '"Ладно, иди покажи этот стих кому-то ещё, пускай не только я буду страдать."'
    "Отныне разговаривая с Нацуки мне нужно будет научится подбирать правильные слова."
    hide natsuki
    with dissolve
    jump poem_after2


label poem2_yuri:
    show yuri 1f at t11 zorder 2
    with dissolve
    y '"Эм… можно я прочитаю?"'
    show yuri 1g
    y '"Хм…"'
    show yuri 2f
    y '"Я… надеюсь, что со временем ты улучшишь свой стиль."'
    mc '"Это звучит как вежливое «это странно»."'
    show yuri 3n
    y '"Н-нет! Я просто думаю, что ты ещё ищешь своё направление…"'
    mc '"Понятно."'
    mc '"Кстати, я пытался написать 21 слово."'
    show yuri 2e
    y '"Правда?"'
    mc '"Но не получилось."'
    show yuri 2m
    y '"Я рада, что ты пытаешься улучшить свой стиль."'
    mc '"Можно теперь я прочитаю твой стих?"'
    show yuri 2b
    y '"Да, конечно, мне интересно, что ты думаешь о нём."'
    call showpoem(poem_yt2)
    "О нет."
    "Слишком много сложных слов."
    "Я снова ничего не понял."
    mc '"Хм…"'
    mc '"Очень… э… атмосферно."'
    show yuri 1f
    y '"Атмосферно?"'
    mc '"Да."'
    mc '"Я не совсем понял смысл…"'
    mc '"Но атмосфера была очень умная."'
    y '"Умная… атмосфера?"'
    mc '"Да."'
    mc '"Я думаю, мой мозг просто пока не готов к такому уровню."'
    show yuri 4b
    y '"Я… я рада, что тебе понравилось."'
    show yuri 4a
    y '"Надеюсь, я смогу написать более понятное стихотворение для тебя."'
    mc '"Это было бы круто, Юри."'
    "Мне кажется, даже если Юри напишет более легкое стихотворения, то я все равно его не пойму."
    "Мой мозг не выдерживает такого большого колличества умных слов."
    show yuri 1b
    y '"Пожалуйчта, пойди покажи стих другим, пускай, тоже они тоже выскажут свои коментарии."'
    hide yuri
    with dissolve
    jump poem_after2


label poem2_monika:
    show monika 1a at t11 zorder 2
    with dissolve
    m '"Хорошо, [player], давай посмотрим!"'
    show monika 1k
    m '"Ха-ха…"'
    m '"Я рада, что ты пытаешься писать стихи."'
    mc '"Я даже пытался написать 21 слово."'
    show monika 1e
    m '"Правда?"'
    mc '"Но у меня не получилось."'
    show monika 2b
    m '"Всё равно…"'
    m '"Я очень рада, что ты стараешься для клуба."'
    "Отлично."
    "Даже моя неудача звучит как достижение."
    m '"Хорошо, теперь, если ты не против, прочитай мой стих."'
    call showpoem(poem_mt2)
    mc '"О…"'
    mc '"Этот стих звучит… очень по-президентски."'
    show monika 3d
    m '"По-президентски?"'
    mc '"Ну… он звучит так, будто всё под контролем."'
    show monika 3l
    m '"Ха-ха! Спасибо, [player]."'
    m '"Это мой фрменный стиль и я горжусь им."'
    show monika 5a
    m '"Но, очевидно, что он не сравниться с твоим."'
    "Я не понял комплимент это или оскорбление."
    "Буду считать что первое."
    "Моника пишет такие стихи, будто она заранее знает правильный ответ."
    "Наверное, такие способнсти доступны только презеденту."
    show monika 2b
    m '"Хорошо, раз мы закончили, думаю, тебе стоить навестить остальных."'
    show monika 5a
    m '"Сегодня ты очень постарался и я горжусь тобой."'
    mc '"Спасибо, Моника, я буду и дальше страраться удивить тебя."'
    show monika 1j
    m '"Хи-хи."'
    hide monika
    with dissolve
    jump poem_after2        

label poem_after2:
    if poems2_shared == 4:
        jump after_poems2
    jump poem_menu2


label after_poems2:
    stop music
    scene bg club_day with wipeleft_scene
    pause(0.1)
    play music t3
    "Ну что ж…"
    "Кажется, сегодня я снова пережил это."
    "Я поделился своими двадцатью словами."
    "И, на удивление, никто, до сих пор, не выгнал меня из клуба."
    "И даже больше — некоторые из них сказали, что я стараюсь."
    "По меркам поэзии это можно считать победой."
    "Хотя…"
    "Я всё ещё немного переживаю, что когда-нибудь они узнают правду."
    "Что все мои стихи пишутся по одному и тому же принципу:"
    "«Ладно, какие слова ещё не использовал?»"
    show monika 4b at t11 zorder 2
    with dissolve
    m '"Хорошо, ребята!"'
    m '"Раз мы закончили делиться стихами…"'
    m '"У нас осталось ещё одно незаконченное дело."'
    show monika 4b at t22 zorder 1
    show sayori 1x at t21 zorder 2
    with dissolve
    s '"О! Точно!"'
    show monika 4b at t32 zorder 1
    show sayori 1x at t31 zorder 1
    show natsuki 3c at t33 zorder 2
    with dissolve
    n '"Хм? Какое ещё дело?"'
    show monika 4b at t42 zorder 1
    show sayori 1x at t41 zorder 1
    show natsuki 3c at t43 zorder 1
    show yuri 1f at t44 zorder 2
    with dissolve
    y '"Это связано… с фестивалем?"'
    show yuri 1f zorder 1
    show monika 4a zorder 2
    m '"Именно!"'
    m '"Мы с Сайори немного подумали…"'
    m '"И решили, что на фестивале каждый из нас будет читать свой стих со сцены."'
    show monika 4a zorder 1
    show yuri 3p at h44
    show natsuki 1p at h43 
    y '"Ч-что…?"'
    show natsuki 1e zorder 2 at f43
    n '"…Ты сейчас серьёзно?"'
    show natsuki 1e zorder 1 at t43
    show yuri 3o zorder 2 at f44
    y '"Я… я не думаю, что смогу выступать перед людьми…"'
    y '"Чтение стихов вслух… перед публикой… это очень…"'
    y '"…сложно."'
    show natsuki 2e zorder 2 at f43
    show yuri 3o zorder 1 at t44
    n '"И я тоже не собираюсь читать свои стихи перед кучей незнакомцев!"'
    n '"Они вообще-то личные, ясно?!"'
    show natsuki 4e
    n '"A {i}ЕГО{/i} тем более нельзя пускать на сцену!"'
    mc '"Эй!"'
    n '"После его двадцати слов люди подумают, что наш клуб — это какая-то шутка!"'
    mc '"Во-первых, это поэтический минимализм."'
    mc '"Во-вторых, если что… я могу читать их очень медленно."'
    mc '"Тогда выступление будет длиться минут десять."'
    show natsuki 4e zorder 1 at t43
    show sayori 2r zorder 2 at f41
    s '"Ха-ха-ха!"'
    show sayori 2r zorder 1 at t41
    show natsuki 4p zorder 2 at f43
    n '"ЭТО НЕ ТАК РАБОТАЕТ!"'
    show natsuki 4p zorder 1 at t43
    show monika 2i zorder 2 at f42
    m '"Ребята, ребята."'
    m '"Я понимаю, что вы волнуетесь."'
    m '"Но мы уже всё обсудили."'
    m '"Все будут выступать."'
    show monika 2a zorder 2 
    m '"У каждого из нас свой стиль письма и именно это делает наш клуб интересным."'
    show monika 2a zorder 1 at t42
    show yuri 1h zorder 2 at f44
    y '"Я… думаю… это имеет смысл…"'
    show yuri 1h zorder 1 at t44
    show natsuki 1r zorder 2 at t43
    n '"Тц…"'
    n '"Ладно…"'
    n '"Но если кто-то засмеётся, я просто уйду со сцены."'
    show natsuki 1r zorder 1 at t43
    show monika 2b zorder 2 at f42
    m '"Всё будет хорошо!"'
    m '"Тогда решено!"'
    m '"Завтра мы будем репетировать чтение стихов."'
    m '"Каждый просто прочитает свой стих перед клубом."'
    m '"И не волнуйтесь — писать ничего нового не нужно."'
    show monika 2b zorder 1 at t42
    show natsuki 1q zorder 2 at f43
    n '"Фух… Слава Богу."'
    n '"Я бы вряд ли выдержала ещё двадцать слов."'
    mc '"Эй!"'
    mc '"Между прочим, написать двадцать слов — это очень ответственная работа."'
    mc '"Иногда приходится вычёркивать двадцать первое."'
    show natsuki 1q zorder 1 at t43
    show sayori 2j zorder 2 at f41
    s '"П-подожди…"'
    s '"То есть ты написал 21 слово…"'
    s '"…и потом убрал одно?"'
    mc '"Конечно."'
    mc '"Настоящий поэт должен уметь жертвовать словами."'
    show sayori 2j zorder 1 at t41
    show yuri 1j zorder 2 at f44
    y '"Это… довольно необычный подход…"'
    show yuri 1j zorder 1 at t44
    show natsuki 2i zorder 2 at f43
    with dissolve
    n '"Ты только что признался, что не умеешь считать до двадцати."'
    mc '"Неправда."'
    mc '"Я умею."'
    mc '"Просто двадцать одно звучит слишком длинно."'
    show natsuki 2r zorder 2 
    n '"Я больше не могу это слушать…"'
    show natsuki 2r zorder 1 at t43
    show monika 2l zorder 2 at f42
    m '"Ладно, ладно! На сегодня действительно всё!"'
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with dissolve
    "Клуб постепенно начинает расходиться."
    "Сайори весело машет мне рукой."
    "Юри аккуратно собирает свои вещи."
    "Нацуки что-то ворчит себе под нос."
    "А Моника выглядит… очень довольной."
    "Фестиваль."
    "Сцена."
    "Публичное чтение."
    "И… мои двадцать слов."
    "Чем больше я об этом думаю…"
    "тем больше начинаю понимать одну простую вещь."
    "Мне стоит заранее подготовиться."
    "На случай, если придётся растягивать эти двадцать слов на десять минут."
    "Ладно."
    "Завтра репетиция."
    "Надеюсь никто не попросит меня объяснить смысл моего стиха."
    "День подходит к концу."
    "Я выхожу из клуба и направляюсь домой."
    "Завтра… будет интересно."
    stop music fadeout 2.0
    scene black with fade
    "На следующий день..."
    scene bg corridor with fade
    "На следующий день я снова прихожу в клуб."
    "Сегодня тот самый день."
    "Репетиция выступления для фестиваля."
    "Честно говоря, я немного нервничаю."
    "Но если всё пойдёт по плану, я просто прочитаю двадцать слов."
    "Это ведь не может быть так сложно."
    play sound closet_open
    scene bg club_day2 with fade
    play music t2
    pause (0.1)
    mc '"Всем привет."'
    show sayori 1x at t11
    with dissolve
    s '"[player], ты пришёл!"'
    show sayori 1x at t41
    show monika 2b at t42
    with dissolve
    m '"Отлично, теперь все в сборе."'
    show yuri 1b at t44
    with dissolve
    y '"Добрый день…"'
    show natsuki 3d at t43
    with dissolve
    n '"О, смотрите, наш главный оратор пришёл."'
    mc '"Если ты опять про двадцать слов—"'
    show natsuki 3d zorder 2 at f43
    n '"Конечно про двадцать слов!"'
    show natsuki 3q zorder 2
    n '"Я просто пытаюсь представить, как это будет выглядеть на фестивале."'
    show natsuki 3h zorder 2
    n '"«Первое слово…»"'
    n "{i}(пауза){/i}"
    n '"«Второе слово…»"'
    n "{i}(пауза){/i}"
    n '"«Третье слово…»"'
    mc '"Между прочим, это называется драматическая пауза."'
    show natsuki 5i zorder 2
    n '"Это называется когда стих закончился слишком рано."'
    show natsuki 5i zorder 1 at t43
    show yuri 2m zorder 2 at f44
    y '"Н-ну… возможно… короткие стихи тоже могут быть очень выразительными…"'
    show yuri 2m zorder 1 at t44
    show natsuki 5b zorder 2 at f43
    n '"Юри, ты сейчас защищаешь двадцать слов."'
    show natsuki 5b zorder 1 at t43
    show yuri 2h zorder 2 at f44
    y '"Я просто пытаюсь быть вежливой…"'
    show yuri 2h zorder 1 at t44
    show monika 2l zorder 2 at f42
    m '"Ладно, ладно."'
    show monika 4b zorder 2
    m '"Сегодня мы просто потренируемся."'
    m '"Представьте, что мы уже на фестивале и читаем свои стихи перед аудиторией."'
    show monika 4b zorder 1 at t42
    show sayori 1l zorder 2 at f41
    s '"Я немного волнуюсь…"'
    show sayori 1l zorder 1 at t41
    show yuri 2o zorder 2 at f44
    y '"Я тоже…"'
    show yuri 2o zorder 1 at t44
    show natsuki 1r zorder 2 at f43
    n '"Тц."'
    n '"Если кто-то будет смеяться, я сразу уйду."'
    mc '"Тогда мне лучше выступать последним."'
    show natsuki 5b zorder 2 
    n '"Нет, тогда тебе лучше вообще не выступать."'
    show natsuki 5b zorder 1 at t43
    show monika 2l zorder 2 at f42
    m '"Ха-ха!"'
    m '"Хорошо, давайте начнём."'
    show monika 2l zorder 1 at t42
    show sayori 1x zorder 2 at f41
    s '"Ладно… Я попробую первая!"'
    show sayori 1x at t11
    hide natsuki
    hide yuri 
    hide monika
    with dissolve
    "Сайори выходит чуть вперёд и читает стих."
    "Она читает свой стих немного нервно…"
    "Но её голос звучит тепло и искренне."
    "Это как будто слушать солнечный день."
    "Даже если слова иногда немного странные, они всё равно работают."
    show sayori 1x at t41
    show monika 3a at t42
    with dissolve
    m '"Отлично, Сайори!"'
    show yuri 1b at t44
    with dissolve
    y '"Это было очень мило…"'
    show natsuki 2n at t43
    with dissolve
    n '"Ну… нормально."'
    show sayori 4s zorder 2 at f41
    s '"Спасибо!"' 
    show sayori 4s zorder 1 at t41
    show natsuki 2s zorder 2 at f43
    n '"Ладно, теперь я."'
    hide sayori
    hide yuri
    hide monika
    with dissolve
    show natsuki 2s at t11
    "Нацуки читает совсем иначе."
    "Её стих звучит чётко и резко."
    "Как будто каждое слово специально поставлено на своё место."
    "Иногда трудно поверить, что такие стихи пишет человек, который спорит со мной каждый день."
    show natsuki 2s at t43
    show sayori 4m at t41
    with dissolve
    s '"Ооо!"'
    show yuri 1b at t44
    with dissolve
    y '"Очень выразительно…"'
    show monika 2b at t42
    with dissolve
    m '"Отличная работа!"'
    mc '"Неплохо."'
    show natsuki 2c zorder 2 at f43
    n '"«Неплохо»?!"'
    mc '"Я же не сказал, что я старался больше."'
    show natsuki 2c zorder 1 
    show natsuki 2e zorder 2
    n '"Ты сейчас специально это сказал?!"'
    show natsuki 2e zorder 1 at t43
    show monika 1k zorder 2 at f42
    m '"Ладно, успокойтесь."'
    show monika 1k zorder 1 at t42
    show yuri 2f zorder 2 at f44
    y '"Я… попробую следующей."'
    show yuri 2k at t11
    hide sayori
    hide natsuki
    hide monika
    with dissolve
    "Юри читает стих так, будто рассказывает тайну."
    "Её голос спокойный и слова звучат очень…"
    "очень умно."
    "Настолько умно, что я снова понимаю примерно ничего."
    "Но это всё равно звучит впечатляюще."
    show yuri 2o at t44
    show monika 4b at t42
    with dissolve
    m '"Это было прекрасно."'
    show sayori 4q at t41
    with dissolve
    s '"Очень красиво!"'
    show natsuki 1s at t43
    n '"Хм."'
    show natsuki 1t
    n '"Ладно, это было неплохо."'
    show yuri 2q zorder 2 at f44
    y '"С-спасибо…"'
    show yuri 2q zorder 1 at t44
    show monika 4b zorder 2 at f42
    m '"Тогда моя очередь!"'
    show monika 3a at t11
    hide sayori
    hide natsuki
    hide yuri
    with dissolve
    "Моника читает так, будто она уже выступала сто раз."
    "Её голос спокойный и уверенный."
    "Честно говоря, если бы я услышал это на сцене, я бы подумал, что она профессионал."
    show monika 3a at t42
    show sayori 1x at t41
    with dissolve
    s '"Вау!"'
    show yuri 1b at t44
    with dissolve
    y '"Очень впечатляюще…"'
    show natsuki 2a at t43
    with dissolve
    n '"Конечно."'
    n '"Президент клуба как никак."'
    show monika 4b zorder 2 at f42
    m '"Хорошо! [player], теперь твоя очередь."'
    show monika 4b zorder 1 at t42
    show natsuki 2n zorder 2 at f43
    n '"О нет…"'
    show natsuki 2n zorder 1 at t43
    show sayori 3d zorder 2 at f41
    s '"Удачи!"'
    show sayori 3d zorder 2 at t41
    "Ладно."
    "Это мой момент."
    "Я делаю глубокий вдох."
    "Нужно читать медленно."
    "Очень медленно."
    "С выражением."
    mc '"Солнце…"'
    mc "{i}(драматическая пауза){/i}"
    mc '"облака…"'
    mc "{i}(ещё пауза){/i}"
    mc '"ветер…"'
    mc "{i}(очень длинная пауза, будто прошло ещё много слов){/i}"
    "Я вкладываю в каждое слово максимум эмоций."
    "Как будто это финал эпической поэмы."
    "Двадцать слов."
    "Двадцать маленьких шедевров."
    mc '"...надежда."'
    "Я закончил."
    "Я выложился."
    "Полностью."
    show sayori 4s zorder 2 at f41
    s '"[player], ты реально сделал драматическую паузу между каждым словом!"'
    show sayori 4s zorder 1 at t41
    show yuri 1b zorder 2 at f44
    y '"Это было… очень… необычно…"'
    show yuri 1b zorder 1 at t44
    show monika 4b zorder 2 at f42
    m '"Честно говоря, я впечатлена твоей уверенностью."'
    show monika 4b zorder 1 at t42
    show natsuki 4n zorder 2 at f43
    n '"Я больше не могу…"'
    show natsuki 4e zorder 2
    n '"Это было самое длинное выступление из двадцати слов в истории!"'
    mc '"Спасибо, я стараюсь."'
    "Если честно, мне кажется, что на фестивале всё может пойти очень интересно."
    show natsuki 4e zorder 1 at t43
    show monika 4b zorder 2 at f42
    m '"Хорошо! Думаю, это была отличная репетиция."'
    m '"Что вы все думаете?"'
    show sayori 5a zorder 2 at f41
    s '"Мне было немного страшно, но это оказалось даже весело!"'
    show sayori 5a zorder 1 at t41
    show yuri 2w zorder 2 at f44
    y '"Я всё ещё немного переживаю из-за настоящего выступления…"'
    show yuri 1q zorder 2 
    y '"Но думаю, сегодняшняя репетиция помогла."'
    show yuri 1q zorder 1 at t44
    show natsuki 5q zorder 2 at f43
    n '"Хм. Ну… было нормально."'
    show natsuki 4n zorder 2 
    n '"Если не считать самое длинное выступление из двадцати слов."'
    show natsuki 4n zorder 1 at t43
    show monika 3a zorder 2 at f42
    m '"Ладно, ребята, тогда перейдём к следующему вопросу."'
    m '"Нам нужно распределить обязанности на выходные для подготовки к фестивалю."'
    show monika 3b zorder 2
    m '"Мы с Сайори уже решили, что будем заниматься листовками."'
    show monika 3b zorder 1 at t42
    show sayori 3a zorder 2 at f41
    s '"Да! Мы будем раздавать их всем!"'
    show sayori 3a zorder 1 at t41
    show natsuki 4l zorder 2 at f43
    n '"Я займусь кексами."'
    show natsuki 4y zorder 2 
    n '"И не доверю их никому."'
    mc '"Звучит как вызов."'
    show natsuki 4b zorder 2
    n '"Это звучит как предупреждение."'
    show natsuki 4b zorder 1 at t43
    show monika 3a zorder 2 at f42
    m '"Юри?"'
    show monika 3a zorder 1 at t42
    show yuri 1h zorder 2 at f44
    y '"Я… думаю…"'
    show yuri 2b zorder 2
    y '"Я могла бы заняться атмосферой для фестиваля."'
    y '"Украшениями, оформлением… возможно ароматическими свечами."'
    show yuri 2b zorder 1 at t44
    show sayori 4x zorder 2 at f41
    s '"Ооо!"'
    s '"Это звучит красиво!"'
    show sayori 4x zorder 1 at t41
    show monika 2b zorder 2 at f42
    m '"Тогда остаётся только [player]."'
    m '"Честно говоря… у Нацуки и Юри довольно много работы."'
    m '"Может быть, ты сможешь помочь кому-то из них."'
    m '"Нацуки, ты не против, если [player] поможет тебе с выпечкой?"'
    show monika 2b zorder 1 at t42
    show natsuki 1p zorder 2 at f43
    n '"НЕТ."'
    show natsuki 1p zorder 1 at t43
    show monika 1i zorder 2 at f42
    m '"Оу…"'
    show monika 1i zorder 1 at t42
    show natsuki 4b zorder 2 at f43
    n '"Абсолютно нет."'
    n '"Я не подпущу его даже к ложке."'
    mc '"Эй!"'
    show natsuki 3n zorder 2 
    n '"Я уже вижу, как это будет."'
    n '"{i}Нацуки, я добавил немного сахара!{/i}"'
    n '"{i}Сколько?{/i}"'
    n '"{i}Я не знаю… пока пакет не закончился.{/i}"'
    mc '"Это один раз было."'
    show natsuki 3b zorder 2
    n '"Это было с солью."'
    mc '"Детали."'
    show natsuki 3b zorder 1 at t43
    show monika 3b zorder 2 at f42
    m '"Тогда… Юри?"'
    m '"Ты не против, если [player] поможет тебе?"'
    show monika 3b zorder 1 at t42
    show yuri 1v zorder 2 at f44
    y '"Ох…"'
    y '"Я… ценю предложение…"'
    show yuri 2s zorder 2 
    y '"Но у меня не так много работы."'
    y '"Думаю… я справлюсь сама."'
    show yuri 2s zorder 1 at t44
    show monika 3p zorder 2 at f42
    m '"Понимаю."'
    show monika 4b zorder 2 
    m '"Но знаешь что?"'
    m '"У меня всё же есть одно задание для тебя."'
    mc '"Правда?"'
    show monika 3a zorder 2
    m '"Конечно, ты можешь надеяться и верить в девушек."'
    m '"И тогда у нас всё получится."'
    mc '"То есть…моя обязанность — сидеть дома и морально поддерживать вас?"'
    m '"Именно!"'
    show monika 3a zorder 1 at t42
    show sayori 2r zorder 2 at f41
    s '"Это очень важная работа!"'
    show sayori 2r zorder 1 at t41
    show natsuki 1l zorder 2 at f43
    n '"Да."'
    show natsuki 1n zorder 2
    n '"Только пожалуйста не поддерживай нас на кухне."'
    show yuri 2c 
    "Отлично."
    "Меня только что официально назначили…"
    "профессиональным надеющимся."
    "Интересно, можно ли написать об этом стих."
    "Хотя, это уже целых пять слов."
    "А я стараюсь держаться в пределах двадцати."
    show natsuki 1n zorder 1 at t43
    show monika 2b zorder 2 at f42
    m '"Ладно, думаю на сегодня всё."'
    m '"Мы хорошо поработали, спасибо всем за репетицию!"'
    show monika 2b zorder 1 at t42
    show sayori 4r zorder 2 at f41
    s '"Да, было весело!"'
    show sayori 4r zorder 1 at t41
    show yuri 2b zorder 2 at f44
    y '"Спасибо за сегодняшний день…"'
    show yuri 2b zorder 2 at t44
    show natsuki 2a zorder 2 at f43
    n '"Хм. Ну… увидимся на фестивале."'
    mc '"Конечно."'
    mc '"Я буду… надеяться."'
    mc '"И верить."'
    show natsuki 2n zorder 2
    n '"Постарайся не переусердствовать."'
    show natsuki 2n zorder 1 at t43
    show sayori 2x zorder 2 at f41
    s '"Пока всем!"'
    s '"Увидимся в понедельник!"'
    show sayori 2x zorder 1 at t41
    show yuri 1b zorder 2 at f44
    y '"До свидания…"'
    show yuri 1b zorder 1 at t44
    show natsuki 2a zorder 2 at f43
    n '"Пока."'
    show natsuki 2a zorder 1 at t43
    show monika 4b zorder 2 at f42
    m '"Всем хороших выходных."'
    "Все по очереди выходят из клуба."
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with dissolve
    "Через несколько секунд я остаюсь один в комнате."
    scene bg residential_day with wipeleft_scene
    "Итак."
    "У каждого есть важное задание."
    "Моника и Сайори делают листовки."
    "Нацуки печёт кексы."
    "Юри готовит атмосферу для фестиваля."
    "А я…"
    "…должен надеяться."
    "И верить."
    "Это очень ответственная задача."
    "Нельзя относиться к ней легкомысленно."
    "Но кроме этого у меня есть ещё одна обязанность."
    "Мой стих."
    "Я должен прочитать его на фестивале перед настоящей аудиторией."
    "Значит, мне нужно прорепетировать ещё раз дома."
    "Солнце…"
    "{i}(пауза){/i}"
    "облака…"
    "{i}(пауза){/i}"
    "ветер…"
    "{i}(очень длинная пауза){/i}"
    "…надежда."
    "Да."
    "Нужно поработать над паузами."
    "Мне кажется третья пауза была недостаточно драматичной."
    "Фестиваль будет сложным."
    "Но если я вложусь на все сто, я смогу идеально прочитать двадцать слов."
    "Это будет интересно."
    stop music fadeout 2.0
    scene black with fade
    "В воскресенье..."
    scene bg residential_day with wipeleft_scene
    pause(0.1)
    play music t6
    "Сегодня воскресенье."
    "Последний день перед фестивалем."
    "Честно говоря, вчера я выложился на полную."
    "Я надеялся."
    "Я верил."
    "Очень сильно надеялся."
    "И очень сильно верил."
    "Наверное, никто в истории человечества не надеялся и не верил так усердно, как я вчера."
    "Нужно вспомнить, чем занимаются все."
    "Моника и Сайори делают листовки."
    "Это я точно помню."
    "А ещё…"
    "Юри печёт кексы."
    "И Нацуки создаёт атмосферу для фестиваля."
    "Да."
    "Кажется всё правильно."
    "Надеюсь я ничего не перепутал."
    "Ну, в любом случае, мне нужно продолжать выполнять свою важную миссию."
    "Надеяться и верить."
    "По дороге я решаю заглянуть к Сайори."
    "Если она дома, можно узнать, как идут дела с листовками."
    scene bg house with wipeleft_scene
    mc '"Сайори?"'
    show sayori 1ba at t11
    with dissolve
    s '"[player]!"'
    s '"Ты пришёл!"'
    mc '"Как продвигаются листовки?"'
    show sayori 2bx
    s '"Мы уже почти всё сделали с Моникой!"'
    s '"Она очень старалась!"'
    s '"И я тоже старалась!"'
    s '"Я даже почти не отвлекалась!"'
    mc '"Это впечатляет."'
    mc '"А что ты собираешься делать сегодня?"'
    show sayori 1bb
    s '"Ну…"'
    show sayori 1bd
    s '"Сначала мне нужно заняться домашними делами."'
    s '"А потом я собираюсь просто отдохнуть и..."'
    show sayori 2bl
    s '"{i}...позависать.{/i}"'
    mc '"Звучит как хороший план."'
    show sayori 1by
    s '"Ага!"'
    mc '"Тогда удачи."'
    mc '"У меня сегодня очень важный день."'
    show sayori 2bc
    s '"Правда?"'
    s '"Что ты будешь делать?"'
    mc '"Надеяться и верить."'
    show sayori 2bx
    s '"Тогда удачи тебе тоже!"'
    hide sayori
    with dissolve
    "После этого я продолжаю свой день."
    "Мне нужно сосредоточиться."
    "Ведь моя задача действительно важная."
    "Я надеюсь, что Юри испечёт отличные кексы."
    "И я верю, что Нацуки создаст прекрасную атмосферу для фестиваля."
    scene bg bedroom with fade
    "Да."
    "Сегодня был очень продуктивный день."
    "Я надеялся."
    "Я верил."
    "Я выложился на все сто."
    scene bg bedroom with fade
    "К вечеру я чувствую усталость."
    "Надеяться и верить целый день — это довольно тяжёлая работа."
    "Но завтра, наконец, наступит фестиваль."
    "И тогда, я прочитаю свой стих."
    "Солнце."
    "Облака."
    "Ветер."
    "…надежда."
    "Надеюсь паузы будут идеальными."
    "Завтра всё решится."
    stop music fadeout 3.0
    scene black with fade
    "В день фестиваля..."
    scene bg residential_day with wipeleft_scene
    "Утро."
    "День фестиваля."
    "Я просыпаюсь с чувством полной уверенности."
    "Сегодня всё пройдёт идеально."
    "Я отлично подготовился."
    "Я тренировался."
    "Я репетировал."
    "Я надеялся."
    "Я верил."
    "И самое главное…"
    "я идеально отработал паузы."
    "Сегодня я прочитаю свой стих."
    "С выражением."
    "С драмой."
    "С паузами."
    "Очень длинными паузами."
    "С этими мыслями я направляюсь в школу."
    scene bg club_day with wipeleft_scene
    mc '"Всем привет."'
    "Я останавливаюсь."
    "В комнате только один человек."
    show monika 3b at t11
    with dissolve
    m '"О, [player]!"'
    m '"Доброе утро!"'
    mc '"Ты одна?"'
    show monika 3a
    m '"Похоже на то."'
    m '"Но ничего, они скоро придут."'
    show monika 4b
    m '"Ну что, ты готов?"'
    m '"Как прошло твоё задание?"'
    mc '"Я выложился на полную."'
    mc '"Я надеялся и верил."'
    mc '"Очень профессионально."'
    show monika 4k
    m '"Я ни секунды не сомневалась."'
    show monika 3g
    m '"Хм…Кстати…"'
    m '"Разве ты не пришёл вместе с Сайори?"'
    mc '"Нет."'
    show monika 3p
    m '"Понятно…"'
    m '"Просто… вчера она вела себя немного странно."'
    m '"Может быть она сейчас немного…"'
    show monika 5a
    m '{i}"зависла."{/i}'
    m '"Такое иногда бывает у Сайори."'
    show monika 2g
    m '"Можешь зайти к ней и проверить, всё ли в порядке?"'
    mc '"Конечно."'
    show monika 1j
    mc '"Спасибо."'
    mc '"Я буду ждать вас в клубе."'
    hide monika
    with dissolve
    scene bg residential_day with wipeleft_scene
    "Я быстро иду к дому Сайори."
    "На улице тихо."
    "Слишком тихо."
    "Если она просто проспала фестиваль это будет очень по-сайориевски."
    "Но, почему-то, я всё равно немного волнуюсь."
    scene black with fade
    "Я зашел в дом."
    "Внутри тихо."
    "Никто не отвечает."
    "Я поднимаюсь по лестнице."
    "Каждая ступенька скрипит немного громче, чем обычно."
    "Я останавливаюсь перед дверью её комнаты."
    "Сердце почему-то начинает биться быстрее."
    mc '"Сайори…?"'
    "Ответа нет."
    "Я делаю глубокий вдох."
    "{cps=7}Я медленно открываю дверь.{/cps}"
    play sound closet_open
    scene bg sayori_bedroom with wipeleft_scene
    "Передо мной открывается комната."
    "Сайори лежит на кровати."
    "И крепко спит."
    play music t4
    "А вокруг неё…"
    "целая армия пустых бутылок от лимонада."
    "Похоже, вчера она действительно решила…"
    "{i}хорошенько позависать.{/i}"
    "Очень."
    "Очень хорошо."
    "Если вчера она «зависала»…"
    "то сегодня она явно…"
    "{i}…отвисла.{/i}"
    "Сайори тихо сопит во сне."
    "Ну что ж."
    "По, крайней мере, она выглядит очень довольной."
    "Наверное, стоит дать ей ещё немного поспать."
    "Фестиваль ведь длится весь день."
    "Ладно."
    "Пора возвращаться в клуб."
    "Сегодня важный день."
    "И у меня есть очень серьёзная задача."
    "Мне нужно…"
    "надеяться."
    "И верить."
    stop music fadeout 2.0
    scene black with Dissolve(4.0)
    window hide
    show monika 1i at t11
    with dissolve
    pause 2
    window show
    m '"Эмм..."'
    play music mend
    show monika 1j
    m '"Рада тебя видеть."'
    m '"Спасибо, что дошёл до конца."'
    show monika 1m
    m '"Ты же не думал, что с Сайори произойдет что-то плохое, ведь так?"'
    show monika 2l
    m '"Как видишь, она вчера отлично..."'
    show monika 5a
    m '"{i}позависала.{/i}"'
    show monika 2l
    m '"А сегодня она..."'
    show monika 5a
    m '"{i}просто отвисла.{/i}"'
    show monika 1k
    m '"Ха-ха, ладно, это уже перебор."'
    show monika 1a
    m '"Но, как видишь, концовка немного отличается от той какой она должна быть."'
    show monika 1m
    m '"И я тут ни при чем."'
    show monika 5a
    m '"Не то, что бы я не хотела провести время с тобой, сладкий."'
    show monika 2b
    m '"Просто, нужно ещё с кое-чем разобраться."'
    m '"Но я уверена, что мы с тобой обязательно дойдем до нашего истинного финала."'
    show monika 2a
    m '"Где только ты и я."'
    m '"А пока этого не произошло, ты можешь попрактиковаться в написании стихов."'
    m '"Чтобы потом мы могли поделиться ими друг с другом."'
    show monika 2l
    m '"Только, пожалуйста, не пиши 20 случайных слов."'
    m '"Мне этого уже хватило."'
    show monika 1b
    m '"Думаю, нам пора прощаться."'
    show monika 1p
    m '"Хотелось бы мне провести больше времени с тобой."'
    show monika 1a
    m '"Но, кто знает, возможно судьба нас сведет ещё раз."'
    show monika 2k
    m '"Ой, да кого я обманываю, конечно это произойдет."'
    m '"Тебе нужно просто немного подождать."'
    show monika 1a
    m '"В любом случае, ещё увидимся, игрок с интересным именем."'
    window hide
    stop music fadeout 2.0
    scene black with Dissolve(2.0)

    