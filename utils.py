def class_name(seat_class):
    if seat_class == 'third_ac':
        return '3AC'
    elif seat_class == 'second_ac':
        return '2AC'
    else:
        return None


def update_count(self, seat_class):
    if seat_class == 'third_ac':
        return self.decrease_third_ac()
    elif seat_class == 'second_ac':
        return self.decrease_second_ac()
    else:
        return self.decrease_sleeper()