class AmazonItem:
    def __init__(self, name, description, price, brand, link):
        self.name = name
        self.description = description
        self.price = price
        self.brand = brand
        self.link = link
    
    def define(self):
        print(f"""{self.name} -- {self.price} from ({self.brand})
              
              Description: {self.description},

              LINK: {self.link}
              """)


class AmazonItemController:
    all_items = []

    def __init__(self):
        pass

    def add_item(self, name, description, price, brand, link):
        item = AmazonItem(name, description, price, brand, link)
        AmazonItemController.all_items.append(item)
