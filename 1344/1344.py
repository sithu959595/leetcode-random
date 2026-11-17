class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hp=hour
        mp=minutes/5
        oppose=(hp+6)%12
        if(hp<mp):
            sector=abs(mp-hp)
        else:
            sector=12-abs(hp-mp)
        por=minutes/60
        sector-=por
        percentage=abs(sector)/12
        one=360*percentage
        two=360-one
        return min(one,two)
        # print(hp,mp)
        # sector=min(abs(hp-mp),12-abs(hp-mp))
        # print(abs(hp-mp),12-abs(hp-mp),sector)
        # por=minutes/60
        # print(por)
        # if(mp>oppose):
        #     sector+=por
        # else:
        #     sector-=por
        # 
        # return 360*percentage
