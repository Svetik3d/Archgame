from archgame import game_server
from archgame import texts
from archgame import events
from archgame import gamers as classes_gamers

FLAG_SLOW_PRINT = False


# Создает экземпляры всех классов
# Запускает главный цикл игры
def game_starter():
    q_g = input(texts.ASK_QUANTITY)
    while not q_g.isdigit():
        print("Введите, пожалуйста, цифру, мы такое не понимаем.")
        q_g = input(texts.ASK_QUANTITY)
    q_g = int(q_g)
    print(texts.ASK_CLASSES)
    gamers = []
    for i in range(1, q_g + 1, 1):
        n, cl = input(texts.ASK_NAME % i).strip().split(",")
        while cl not in ["M", "М", "A", "А", "P", "Р",
                         "m", "м", "a", "а", "p", "р"]:
            print("Неверно введен класс")
            n, cl = input(texts.ASK_NAME % i).strip().split(",")
        if cl in ["M", "М", "m", "м"]:
            cl = "M"
        if cl in ["A", "А", "a", "а"]:
            cl = "A"
        if cl in ["P", "Р", "p", "р"]:
            cl = "P"
        gamers.append(classes_gamers.Gamer(n.strip(), cl.strip(),
                                           FLAG_SLOW_PRINT))
    print(texts.LEGEND)
    ev = events.Events()
    gserv = game_server.GameServer(gamers, ev)
    gserv.main_cycle()


if __name__ == "__main__":
    game_starter()