from market import db
from sqlalchemy.orm import Mapped, mapped_column


class Item(db.Model):  # type: ignore
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    barcode: Mapped[int] = mapped_column(nullable=False, unique=True)
    price: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self):
        return f"<Item (name: {self.name}, price: {self.price})>"
