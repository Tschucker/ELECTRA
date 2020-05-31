class Person: 
    def __init__(self, id_num, locs):
        self.id_num = id_num
        self.locs = locs
        self.infected = False
        self.contacts = []
        self.decypted_attempts = []
        self.alg_contacts = []
    
class Location:
    def __init__(self, day, time, x, y):
        self.day = day
        self.time = time
        self.pos = (x, y)
        self.cell = None
        self.data_id = None
        
class EDataPair:
    def __init__(self, iv, edata):
        self.iv = iv
        self.edata = edata