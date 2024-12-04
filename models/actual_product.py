class ActualProduct:
    def __init__(self, product_id, title, price, discount_percentage):
        self.id = product_id
        self.title = title
        self.price = price
        self.discount_percent = discount_percentage
        self.calculated_price = round(self.calculate_final_price(), 2)

    def calculate_final_price(self):
        return self.price - (self.price * self.discount_percent / 100)
