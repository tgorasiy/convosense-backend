from sqlalchemy import Column, String, DateTime, Enum, ForeignKey, Text, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime
from .base import Base

class RoleEnum(str, Enum):
CUSTOMER = "customer"
AGENT = "agent"
ADMIN = "admin"

class User(Base):
__tablename__ = "users"
id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
email = Column(String, unique=True, index=True, nullable=False)
name = Column(String, nullable=False)
role = Column(String, default="customer", nullable=False)
hashed_password = Column(String, nullable=False)
created_at = Column(DateTime, default=datetime.utcnow)
tickets = relationship("Ticket", back_populates="creator")

class Ticket(Base):
__tablename__ = "tickets"
id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
title = Column(String, nullable=False)
description = Column(Text, nullable=False)
status = Column(String, default="open") # open | in-progress | resolved
intent = Column(String, nullable=True)
sentiment = Column(String, nullable=True)
creator_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
assignee_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
created_at = Column(DateTime, default=datetime.utcnow)
updated_at = Column(DateTime, default=datetime.utcnow)

creator = relationship("User", foreign_keys=[creator_id], back_populates="tickets")
# optional: relationship to assignee via alias

class ChatMessage(Base):
__tablename__ = "chat_messages"
id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
role = Column(String, default="user") # user|assistant|system
content = Column(Text, nullable=False)
ticket_id = Column(UUID(as_uuid=True), ForeignKey("tickets.id"), nullable=True)
created_at = Column(DateTime, default=datetime.utcnow)