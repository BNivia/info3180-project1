from . import db

class Properties(db.Model):
    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(60))
    description = db.Column(db.String(255))
    beds = db.Column(db.Integer)
    baths = db.Column(db.Integer)
    location = db.Column(db.String(50))
    price = db.Column(db.String(20))
    ptype = db.Column(db.String(10))
    img = db.Column(db.String(255))

    def __init__(self,title,description,beds,baths,location,price,ptype,img):
        self.title = title
        self.description = description
        self.beds = beds
        self.baths = baths
        self.location = location
        self.price = price
        self.ptype = ptype
        self.img = img