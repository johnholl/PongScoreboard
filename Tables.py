from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, create_engine, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, foreign



engine = create_engine('sqlite:///database.db')
Base = declarative_base()


class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	detail = Column(String)
	sound = Column(String)

	games = relationship(
		"Game",
		primaryjoin=lambda: or_(
			User.id == foreign(Game.player1_id),
			User.id == foreign(Game.player2_id)
		),
		viewonly=True,
	)

	def __repr__(self):
		return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)


class Game(Base):
	__tablename__ = 'game'
	id = Column(Integer, primary_key=True)
	player1_id = Column(Integer, ForeignKey('user.id'))
	player2_id = Column(Integer, ForeignKey('user.id'))
	p1score = Column(Integer)
	p2score = Column(Integer)
	p1winner = Column(Boolean)

	player1 = relationship("User", foreign_keys=player1_id)
	player2 = relationship("User", foreign_keys=player2_id)

	def __repr__(self):
		return "<Game(player1='%s', player2='%s')>" % (self.player1, self.player2)


# Base.metadata.create_all(engine)
