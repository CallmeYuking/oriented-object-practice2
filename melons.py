"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty, order_type, tax, shipped):
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = shipped

    def get_total(self, base_price = 5,):
        """Calculate price, including tax."""

        if self.species == 'Christmas melon':
            total = (1 + self.tax) * self.qty * (base_price * 1.5)
        else:
            total = (1 + self.tax) * self.qty * base_price

        return total + self.flat_fee

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
        

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, 'domestic', 0.08, False)
        
        self.flat_fee = 0


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        self.country_code = country_code
        super().__init__(species, qty, "international", 0.17, False)

        if qty < 10:
           self.flat_fee = 3
        else:
            self.flat_fee = 0
        

    def get_country_code(self):
        """Return the country code."""
        return self.country_code


    


        
