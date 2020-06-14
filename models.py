from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from typing import Any

class Achievement():
    __tablename__ = "achievements"
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	points_value = Column(Integer, nullable=False)
	
	def __init__(self, **kwargs: Any) -> str:
		super(Achievement, self).__init__(**kwargs) 		
	
	
class User():
	__tablename__ = "users"
	id = Column(Integer, primary_key=True)
	#discord_id = Column(string, nullable=False)
	username = Column(String, nullable=False)
	
	def __repr__(self, **kwargs: Any) -> str:
		super(User, self).__init__(**kwargs)
		return f"<User - ID: {self.id}, username: {self.username}>"
	
class UserAchievement():
	__tablename__ = "user_achievements"
	id = Column(Integer, primary_key=True)
	achievementId = Column(Integer, ForeignKey("achiements.id"))
	userId = Column(Integer, ForeignKey("users.id"))
	achievementReceivedUtc = Column(DateTime)
	
	def __repr__(self, **kwargs: Any) -> str:
		super(UserAchievement, self).__init__(**kwargs)
		return f"UserAchievement ID: {self.id}, userId: {self.userId}, achiementId: {self.achiementId}>"