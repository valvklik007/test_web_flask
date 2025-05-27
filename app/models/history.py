from app import db
from datetime import datetime

class SearchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_ip = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"<SearchHistory city={self.city} time={self.timestamp}>"

