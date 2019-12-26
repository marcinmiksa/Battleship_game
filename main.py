from Game import Game


def main():
    try:
        game = Game()
        game.run()
    except KeyboardInterrupt:
        exit(0)
    except ValueError:
        print('\nNieprawidlowy symbol wejsciowy')
        exit(1)

if __name__ == '__main__':
    main()
