from Game import Game


def main():
    try:
        game = Game()
        game.create_view()
        game.put_ships()
        game.run()
    except ValueError:
        print('\nNieprawidlowy symbol wejsciowy')


if __name__ == '__main__':
    main()
