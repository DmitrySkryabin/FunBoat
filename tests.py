import pytest
from fun_boat import FunBoat 


@pytest.fixture
def boat():
    return FunBoat()


@pytest.fixture
def boat_with_rowers(boat: FunBoat):
    '''
    Возращаем лодку уже с гребцами
    '''
    boat.add_rowers(3)
    return boat


def test_add_rowers(boat: FunBoat):
    boat.add_rowers(2)
    assert boat.get_status()['rowers'] == 2


def test_add_too_many_rowers(boat: FunBoat):
    boat.add_rowers(5)
    with pytest.raises(ValueError, match="To many rowers"):
        boat.add_rowers(2)


def test_remove_rowers(boat_with_rowers: FunBoat):
    boat_with_rowers.remove_rowers(1)
    assert boat_with_rowers.get_status()['rowers'] == 2


def test_remove_too_many_rowers(boat_with_rowers: FunBoat):
    with pytest.raises(ValueError, match="Cant remove more rowers"):
        boat_with_rowers.remove_rowers(4)


def test_start_rowing_without_rowers(boat: FunBoat):
    with pytest.raises(RuntimeError, match="Cant row without rowers"):
        boat.start_rowing()
        

def test_start_and_stop_rowing(boat_with_rowers: FunBoat):
    boat_with_rowers.start_rowing()
    status = boat_with_rowers.get_status()
    assert status['is_moving'] is True
    assert status['speed'] == 3 * 0.8

    boat_with_rowers.stop_rowing()
    status = boat_with_rowers.get_status()
    assert status['is_moving'] is False
    assert status['speed'] == 0


def test_turning_while_moving(boat_with_rowers: FunBoat):
    boat_with_rowers.start_rowing()
    boat_with_rowers.turn('e')
    assert boat_with_rowers.get_status()['direction'] == 'e'


def test_turning_invalid_direction(boat_with_rowers: FunBoat):
    boat_with_rowers.start_rowing()
    with pytest.raises(ValueError, match="Direction must be"):
        boat_with_rowers.turn('invalid')


def test_turning_while_stopped(boat_with_rowers: FunBoat):
    with pytest.raises(RuntimeError, match="Cant turn when boat not moving"):
        boat_with_rowers.turn('n')
        
        
def test_start_funning(boat_with_rowers: FunBoat):
    boat_with_rowers.start_funning()
    assert boat_with_rowers.get_status()['song_power'] == 150
    
    
def test_start_funning_without_rowers(boat: FunBoat):
    with pytest.raises(RuntimeError, match="No one to sing songs"):
        boat.start_funning()


def test_stop_funning(boat_with_rowers: FunBoat):
    boat_with_rowers.start_funning()
    boat_with_rowers.stop_funning()
    assert boat_with_rowers.get_status()['song_power'] == 0


def test_full_scenario(boat: FunBoat):
    boat.add_rowers(4)
    boat.start_funning()
    boat.start_rowing()
    boat.turn('s')
    boat.remove_rowers(2)
    boat.stop_rowing()
    status = boat.get_status()

    assert status == {
        'rowers': 2,
        'is_moving': False,
        'direction': 's',
        'speed': 0,
        'song_power': 100
    }
