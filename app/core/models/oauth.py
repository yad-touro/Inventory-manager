from datetime import datetime
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin
from app import db

class OAuth(OAuthConsumerMixin, db.Model):
    """OAuth token storage model."""
    __tablename__ = 'oauth'

    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(50), nullable=False)
    provider_user_id = db.Column(db.String(256), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('oauth_tokens', lazy='dynamic'))

    def __repr__(self):
        return f'<OAuth {self.provider}:{self.provider_user_id}>' 