import unittest
from shoppingCart import ShoppingCart, Item

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        item = Item('apple', 2.0, 5)
        self.cart.add_item(item)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].name, 'apple')
        self.assertEqual(self.cart.items[0].price, 2.0)
        self.assertEqual(self.cart.items[0].quantity, 5)

    def test_total_price(self):
        self.cart.add_item(Item('apple', 2.0, 5))
        self.cart.add_item(Item('banana', 1.5, 3))
        self.assertEqual(self.cart.total_price(), 2.0 * 5 + 1.5 * 3)

    def test_remove_item(self):
        item = Item('apple', 2.0, 5)
        self.cart.add_item(item)
        self.cart.remove_item('apple')
        self.assertEqual(len(self.cart.items), 0)

    def test_remove_item_not_in_cart(self):
        with self.assertRaises(ValueError):
            self.cart.remove_item('orange')

    def test_empty_cart(self):
        
        self.cart.add_item(Item('apple', 2.0, 5))
        self.cart.empty_cart()
        self.assertEqual(len(self.cart.items), 0)

if __name__ == '__main__':
    unittest.main()
