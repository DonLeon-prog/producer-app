import uuid
from datetime import datetime

from sqlalchemy import Column, String, Integer, Date, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    telegram_id = Column(String, unique=True, nullable=False, index=True)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    user_type = Column(String, nullable=True)  # "blogger" | "musician"
    profile = Column(JSON, nullable=True)
    plan = Column(String, default="free", nullable=False)  # "free" | "pro" | "producer"
    requests_today = Column(Integer, default=0, nullable=False)
    last_request_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
