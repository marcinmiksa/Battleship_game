class Stats:
    ship_counter = 0

    def __init__(self):
        self.tries_count = 0
        self.missed_shots_count = 0
        self.successful_shots_count = 0

    def increase_tries_count(self):
        self.tries_count += 1

    def increase_missed_shots_count(self):
        self.missed_shots_count += 1
        self.increase_tries_count()

    def increase_successful_shots_count(self):
        self.successful_shots_count += 1
        self.increase_tries_count()

    def display_stats(self):
        print('*** Statystyki ***')
        print('Trafione strzaly: {}'.format(self.successful_shots_count))
        print('Chybione strzaly: {}'.format(self.missed_shots_count))
        print('Laczna liczba strzalow: {}'.format(self.tries_count))


