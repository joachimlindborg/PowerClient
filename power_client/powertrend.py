# Powertrend visulasier that can show if the swedish powergrid is importing or exporting
# depends on ssd1d1306 oled display
# micropython basic urequests and of course time

import urequests

#If you dont have a display just a plain device 
import ssd1306
import time

# some debug starting point for the display
#ssd.text("hello world",0,0)
#ssd.text("1234567890123456",0,10)
#ssd.show()
SET_EXPORT="fin el"
#SET_EXPORT="EXPORT"
SET_IMPORT="ful el"
#SET_IMPORT="IMPORT"
SET_AUTH_TOKEN='YourFantasticTokenFromThe my.Live-in.se account !!!'

class Powertrend:
    def __init__(self,i2c):
        self.graf=[]
        self.ssd=ssd1306.SSD1306_I2C(128,32,i2c)
        self.ssd.fill(0)
        self.ssd.show()

    def get_the_gridstatus(self,auth_token=SET_AUTH_TOKEN):
        headers={'Authorization':'Bearer '+auth_token}
        respons=urequests.post('https://my.live-in.se/api/powerstatus',headers=headers)
        return respons.json()['status']

    def display(self,status,graf):
        graf_height=10
        graf_offset_y=20
        pix_len=graf_height/100
        self.ssd.fill(0)
        if status['output']:
            self.ssd.text("EXPORT",0,0)
        else:
            self.ssd.text("IMPORT",0,0)
        self.ssd.text(str(status['facility']),60,0)
        self.ssd.text(status['trend'][0:3],100,0)
        pos=0
        for line in graf:
            line_lenth=round(pix_len*line)
            if line_lenth==0:
                line_lenth=1
            if line_lenth>0:
                for each_pixel in range(0,line_lenth):
                    # print("pixel "+str(pos)+'x'+ str(each_pixel+graf_offset_y))
                    self.ssd.pixel(pos,each_pixel+graf_offset_y,1)
            else:
                for each_pixel in range(line_lenth,0):
                    # print("pixel "+str(pos)+'x'+ str(each_pixel+graf_offset_y))
                    self.ssd.pixel(pos,each_pixel+graf_offset_y,1)
            pos+=1
        self.ssd.show()

    def add_graf_value(self,value):
        self.graf.append(value)
        if len(self.graf)>128:
            self.graf.pop(0)
        
    def main_run(self):
        while True:
            print(str(time.ticks_ms()))
            status=self.get_the_gridstatus()
            self.add_graf_value(status['facility']*(status['output']*-1))
            print(str(status))
            # just comment this line to just show the debug information
            self.display(status,self.graf)
            time.sleep(120)
    
