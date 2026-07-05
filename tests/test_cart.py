import unittest
from decimal import Decimal

from src.cart import CartItem, calculate_final_price, calculate_subtotal


class CartCalculationTest(unittest.TestCase):
    def test_calculate_subtotal_for_multiple_items(self):
        items = [
            CartItem("notebook", Decimal("6.50"), 2),
            CartItem("pen", Decimal("1.20"), 3),
        ]

        self.assertEqual(calculate_subtotal(items), Decimal("16.60"))

    def test_rejects_non_positive_quantity(self):
        item = CartItem("eraser", Decimal("2.00"), 0)

        with self.assertRaises(ValueError):
            item.line_total()

    def test_calculate_final_price_with_discount(self):
        items = [
            CartItem("book", Decimal("20.00"), 1),
            CartItem("coupon item", Decimal("10.00"), 1),
        ]

        self.assertEqual(calculate_final_price(items, Decimal("0.5")), Decimal("15.00"))

    def test_calculate_final_price_with_zero_discount(self):
        items = [CartItem("book", Decimal("20.00"), 1)]

        self.assertEqual(calculate_final_price(items, Decimal("0")), Decimal("20.00"))

    def test_calculate_final_price_with_full_discount(self):
        items = [CartItem("book", Decimal("20.00"), 1)]

        self.assertEqual(calculate_final_price(items, Decimal("1")), Decimal("0.00"))

    def test_calculate_final_price_rounds_to_cents(self):
        items = [CartItem("book", Decimal("19.99"), 3)]

        self.assertEqual(calculate_final_price(items, Decimal("0.15")), Decimal("50.97"))

    def test_rejects_discount_rate_below_zero(self):
        items = [CartItem("book", Decimal("20.00"), 1)]

        with self.assertRaises(ValueError):
            calculate_final_price(items, Decimal("-0.01"))

    def test_rejects_discount_rate_above_one(self):
        items = [CartItem("book", Decimal("20.00"), 1)]

        with self.assertRaises(ValueError):
            calculate_final_price(items, Decimal("1.01"))


if __name__ == "__main__":
    unittest.main()
