from market import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, select
from market import bcrypt, login_manager, db
from flask_login import UserMixin  # type: ignore


@login_manager.user_loader
def load_user(user_id):
    stmt = select(User).where(User.id == user_id)
    return db.session.execute(stmt).scalars().first()


class User(Base, UserMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    email_address: Mapped[str] = mapped_column(nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    balance: Mapped[int] = mapped_column(nullable=False, default=1000)
    items: Mapped[list["Item"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"<User (username: {self.username}, email: {self.email_address})>"

    def check_password(self, text_password):
        return bcrypt.check_password_hash(self.password_hash, text_password)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, text_password):
        self.password_hash = bcrypt.generate_password_hash(text_password).decode(
            "utf-8"
        )


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
