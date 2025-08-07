class FunBoat:

    BOAT_CAPACITY = 6 # Вместимость лодки
    DIRECTION = ['n', 'w', 's', 'e']
    
    def __init__(self):
        self.rowers = 0 # Гребцы
        self.is_moving = False 
        self.direction = 'n' # Начальное направление на север
        self.speed = 0
        
    def __udpate_speed(self):
        if self.is_moving:
            self.speed = self.rowers * 0.8 # Взял с головы, типа 2 гребца не гребят в 2 раза больше 1
        else:
            self.speed = 0
        
    def add_rowers(self, count_of_rowers):
        if self.rowers + count_of_rowers > self.BOAT_CAPACITY:
            raise ValueError('To many rowers')
        self.rowers += count_of_rowers
        
    def remove_rowers(self, count_of_rowers):
        if self.rowers - count_of_rowers < 0:
            raise ValueError('Cant remove more rowers than you have')
        self.rowers -= count_of_rowers
        
    def start_rowing(self):
        if self.rowers == 0:
            raise RuntimeError('Cant row without rowers')   
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
            raise ValueError('Direction must be: "n", "w", "s", "e"')
        if not self.is_moving:
            raise RuntimeError('Cant turn when boat not moving')
        self.direction = direction
        
    def get_status(self):
        return {
            'rowers': self.rowers,
            'is_moving': self.is_moving,
            'direction': self.direction,
            'speed': self.speed
        }