from market import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    email_address: Mapped[str] = mapped_column(nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    items: Mapped[list["Item"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"<User (username: {self.username}, email: {self.email_address})>"


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    barcode: Mapped[int] = mapped_column(nullable=False, unique=True)
    price: Mapped[int] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="items")

    def __repr__(self):
        return f"<Item (name: {self.name}, price: {self.price})>"
