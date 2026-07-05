from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class CartItem:
    name: str
    unit_price: Decimal
    quantity: int

    def line_total(self) -> Decimal:
        if self.quantity <= 0:
            raise ValueError("quantity must be positive")
        if self.unit_price < Decimal("0"):
            raise ValueError("unit_price must not be negative")
        return self.unit_price * self.quantity


def calculate_subtotal(items: list[CartItem]) -> Decimal:
    return sum((item.line_total() for item in items), Decimal("0"))

