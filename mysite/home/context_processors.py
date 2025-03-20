from .cart import Cart

#Create contect processor so out my courses can work on all pages
def cart(request):
    #retrun the default data from our My_course
    return {'cart': Cart(request) }