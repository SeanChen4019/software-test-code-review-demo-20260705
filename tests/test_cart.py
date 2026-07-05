import unittest
from decimal import Decimal

from src.cart import CartItem, calculate_subtotal


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


if __name__ == "__main__":
    unittest.main()

