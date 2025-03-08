from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table, DateTime, func
from sqlalchemy.orm import relationship, declarative_base
from passlib.context import CryptContext
from datetime import datetime

Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

user_applications = Table(
    "user_applications",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("application_id", Integer, ForeignKey("applications.id"), primary_key=True),
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    applications = relationship("Application", secondary=user_applications, back_populates="users")

    def set_password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    users = relationship("User", secondary=user_applications, back_populates="applications")
    roles = relationship("Role", back_populates="application")

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    application_id = Column(Integer, ForeignKey("applications.id"))

    application = relationship("Application", back_populates="roles")
    users = relationship("UserRole", back_populates="role")

class UserRole(Base):
    __tablename__ = "user_roles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    application_id = Column(Integer, ForeignKey("applications.id"), nullable=False)

    user = relationship("User")
    role = relationship("Role", back_populates="users")
    application = relationship("Application")
