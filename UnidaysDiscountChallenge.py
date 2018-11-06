class UnidaysDiscountChallenge():
    def __init__(self, PricingRules=
                 {'A': [8, (0, 0)],
                  'B': [12, (2, 20)],
                  'C': [4, (3, 10)],
                  'D': [7, (2, 7)],
                  'E': [5, (3, 10)]}):
        '''Multi-line comment:
            The question appeared to be a bit vague in describing how the pricing rules were to be initialised
            It did not mention how to specify the discount column since it was provided as strings of varying kinds.
            eg: 2 for 20, 3 for the price of 2, Buy 1 get 1 free.
            The most logical way of solving this problem would have been to make a natural language parser but that
            would also be over-complicating the problem.
            Therefore, I have defined PricingRules as a dictionary where the key is the name of the item provided
            and the value is a list where the first element is the price of a single item and the second element is a tuple
            whose first element is the number of items that qualify you for the discount, and the second element is the
            total price for that many items after the discount.
            In the part of the question where example use cases of the Interface were shown on GitHub,
            the object of this class was made using a pricingRules argument.
            Therefore I have made an optional argument in this constructor for the same.
            Please keep in mind that the data structure I have defined above must be used to pass the argument
            in order to maintain the integrity and functionality of the application.'''
        self.PricingRules = PricingRules
        self._Basket = {}#key=item, value=quantity

    def getBasket(self):
        return self._Basket
    
    def AddToBasket(self, items):#it would be more convenient to pass a quantity as an additional argument, but I'm sticking to the specifics outlined by the question
        #in the example test cases in the 'Items' column, you have provided strings that specify all the items to be added to the basket
        #I'm working with this model now
        for item in items:
            if item in self.PricingRules:
                if item in self._Basket:
                    self._Basket[item] += 1
                else:
                    self._Basket[item] = 1
            else:
                print("ERROR: Item ("+item+") not found in database")
            
    def CalculateTotalPrice(self):
        total = 0
        delivery = 0
        basket = self.getBasket()
        for key in basket:
            #for each key in basket, find the number of times PricingRules[key][1][0] goes into basket[key]
            #multiply this number with PricingRules[key][1][1] to get the discounted rate
            #add this number to the total
            #subtract the quantity already used from basket[key] and
            #then add PricingRules[key][0]*basket[key] (where basket[key] is the number after the subtraction
            discountQuantity = 0
            try:
                discountQuantity = basket[key]//self.PricingRules[key][1][0]
            except:
                pass
            total += self.PricingRules[key][1][1]*discountQuantity
            basket[key] -= discountQuantity*self.PricingRules[key][1][0]
            total += self.PricingRules[key][0]*basket[key]
        if total<50:
            delivery = 7
        price = Price(total, delivery)
        return price
            
        
    

class Price():
    def __init__(self, Total, DeliveryCharge):
        self.Total = Total
        self.DeliveryCharge = DeliveryCharge
