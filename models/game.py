from main import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    platform = db.Column(db.String(50), nullable=False)
    completed = db.Column(db.models.Boolean)

    def __repr__(self):
        return '<Name %r>' % self.name