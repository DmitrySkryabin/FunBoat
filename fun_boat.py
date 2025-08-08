import logging

class FunBoat:

    BOAT_CAPACITY = 6  # Вместимость лодки
    DIRECTION = ['n', 'w', 's', 'e']

    LOG = logging.getLogger(__name__)

    def __init__(self):
        self.rowers = 0  # Гребцы
        self.is_moving = False 
        self.direction = 'n'  # Начальное направление на север
        self.speed = 0
        self.song_power = 0  # Громкость песни

    def __udpate_speed(self):
        if self.is_moving:
            self.speed = self.rowers * 0.8  # Взял с головы, 2 гребца не гребут в 2 раза больше 1
        else:
            self.speed = 0
        self.LOG.info(f'Speed updated: {self.speed}')

    def __update_song_power(self):
        self.song_power = self.rowers * 50  # Примерные герцы
        self.LOG.info(f'Song power updated: {self.song_power}')

    def add_rowers(self, count_of_rowers):
        if self.rowers + count_of_rowers > self.BOAT_CAPACITY:
            raise ValueError('Too many rowers. Boat capacity exceeded.')
        self.rowers += count_of_rowers
        self.__update_song_power()

    def remove_rowers(self, count_of_rowers):
        if self.rowers - count_of_rowers < 0:
            raise ValueError('Cannot remove more rowers than are present.')
        self.rowers -= count_of_rowers
        self.__update_song_power()

    def start_rowing(self):
        if self.rowers == 0:
            raise RuntimeError('Cannot start rowing without rowers.')
        self.is_moving = True
        self.__udpate_speed()

    def stop_rowing(self):
        self.is_moving = False
        self.__udpate_speed()

    def turn(self, direction: str):
        '''
        Поворачиваем лодку в направлении стороны света

        Args:
            direction (str): Сторона света:
                - n: Север
                - w: Запад
                - s: Юг
                - e: Восток
        '''
        if direction not in self.DIRECTION:
            raise ValueError('Direction must be one of: "n", "w", "s", "e".')
        if not self.is_moving:
            raise RuntimeError('Cannot turn while the boat is not moving.')
        self.direction = direction

    def start_funning(self):
        '''
        Делаем лодку веселой
        '''
        if self.rowers == 0:
            raise RuntimeError('Cannot start funning without rowers.')
        self.__update_song_power()
        self.LOG.info(f'Yo, Ho haul together, hoist the colours high...')

    def stop_funning(self):
        '''
        Делаем лодку не веселой
        '''
        self.song_power = 0
        self.LOG.info(f'Silence over the water surface')

    def get_status(self):
        return {
            'rowers': self.rowers,
            'is_moving': self.is_moving,
            'direction': self.direction,
            'speed': self.speed,
            'song_power': self.song_power
        }

logging.basicConfig(level=logging.INFO)
