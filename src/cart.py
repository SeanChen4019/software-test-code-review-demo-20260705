from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP


CENTS = Decimal("0.01")


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


def calculate_final_price(items: list[CartItem], discount_rate: Decimal) -> Decimal:
    rate = Decimal(str(discount_rate))
    if rate < Decimal("0") or rate > Decimal("1"):
        raise ValueError("discount_rate must be between 0 and 1")

    subtotal = calculate_subtotal(items)
    final_price = subtotal * (Decimal("1") - rate)
    return final_price.quantize(CENTS, rounding=ROUND_HALF_UP)
