

class Alarm_clock:

    def __init__(self):
        self.current_time = ''
        self.power = ''
        self.alarm_time = ''

    def change_current_time(self):
        self.current_time = input('Enter current time ')
        
       

    def toggle_alarm_on_or_off(self):
            if input('on or off').lower == 'off':
                print('Alarm turned off ')
                self.power ='off'
            else:
                print('Alarm turned on')
                self.power ='on'
               
                

    

    def set_alarm_time(self):
       self.alarm_time = input('Enter time of alarm to be set ')
       
       
