from Stock_Manager import db

class Part(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    manufacturer    = db.Column(db.String(40))
    orderingCode    = db.Column(db.String(40))
    case_id         = db.Column(db.Integer, db.ForeignKey('package.id'))

    def __init__(self, manufacturer, orderingCode, case_id):
        self.manufacturer   = manufacturer
        self.orderingCode   = orderingCode
        self.case_id        = case_id

    def __repr__(self):
        return '<Part: %r %r>' % (self.manufacturer, self.orderingCode) 


class Package(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(30), unique=True)
    pin_count       = db.Column(db.Integer)
    pitch           = db.Column(db.Float)
    width           = db.Column(db.Float)
    length          = db.Column(db.Float)
    height          = db.Column(db.Float)
    alt_names       = db.relationship('AltPackage', backref='package', lazy='dynamic')
    parts           = db.relationship('Part', backref='package', lazy='dynamic')

    def __init__(self, name, pin_count, pitch, width, length, height):
        self.name            = name
        self.pin_count       = pin_count
        self.pitch           = pitch
        self.width           = width
        self.length          = length
        self.height          = height

    def __repr__(self):
        return '<Package: %r>' % self.name

class AltPackage(db.Model):
    id                  = db.Column(db.Integer, primary_key=True)
    name                = db.Column(db.String(20), unique=True)
    parent_package_id   = db.Column(db.Integer, db.ForeignKey('package.id'))

    def __init__(self, name, parent_id):
        self.name = name
        self.parent_package_id = parent_id
#        self.parent_case_id = parent_case_id
    
    def __repr__(self):
        return '<Case Alternate name: %r>' % self.name

# class DistributorOfPart(db.Model):
#     id              = db.Column(db.Integer, primary_key=True)
#     partId          = db.Column(db.Integer, db.ForeignKey('Part.id'))
#     distributor     = db.Column(db.String(20))
#     orderingCode    = db.Column(db.String(40))
#     priceEur100     = db.Column(db.Float)
#     priceEur10k     = db.Column(db.Float)

#     part = db.relationship('Part')
    
#     def __init__ (partId, distributor, orderingCode, priceEur100, priceEur10k = 0):
#         self.partId         = partId
#         self.distributor    = distributor
#         self.orderingCode   = orderingCode
#         self.priceEur100    = priceEur100
#         self.priceEur10k   = priceEur10k
    
#     def __repr__(self):
#         return '<Distributor %r for %r>' % (self.dsitributorName, self.orderingCode)