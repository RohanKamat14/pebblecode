from .models import Product

class Cart():

    def __init__(self, request):
        
        self.session = request.session
        # get the current session key ifit exists
        cart = self.session.get('session_key')
        # if the user is new, no session key! creating one.
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        #make sure course is available on all pages of the site
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'name': str(product.name)}
        
        self.session.modified = True



    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #get ids from cart
        product_ids = self.cart.keys()
        # use ids to look up products in the database model
        products = Product.objects.filter(id__in=product_ids)

        return products