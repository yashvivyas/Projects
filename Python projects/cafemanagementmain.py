#main
actions= {
    'view menu':1,
    'add item':2,
    'view cart':4,
    'remove item':3,
    'finish order':5,
    'get bill':6
}

#menu dictionary
menu= [
    {'id':1, 'name': 'Americano', 'price':120},
    {'id':2, 'name': 'Cappucino', 'price':150},
    {'id':3, 'name': 'Espresso', 'price':100},
    {'id':4, 'name': 'Latte', 'price':180},
    {'id':5, 'name': 'Matcha Latte', 'price':200},
    {'id':6, 'name': 'Chai Tea', 'price':20},
    {'id':7, 'name': 'Green Tea', 'price':100},
    {'id':8, 'name': 'Iced Tea', 'price':100},
    {'id':9, 'name': 'Vanilla Shake', 'price':150},
    {'id':10, 'name': 'Chocolate Shake', 'price':150},
    {'id':11, 'name': 'Strawberry Shake', 'price':150},
    {'id':12, 'name': 'Oreo Shake', 'price':150},
    {'id':13, 'name': 'Banana Shake', 'price':150},
    {'id':14, 'name': 'Fruit Smoothie', 'price':150},
    {'id':15, 'name': 'Peanut Butter Shake', 'price':150},
    {'id':16, 'name': 'Mint Mojito', 'price':150},
    {'id':17, 'name': 'Orange Mojito', 'price':150},
    {'id':18, 'name': 'Strawberry Mojito', 'price':150},
    {'id':19, 'name': 'Blackcurrant Mojito', 'price':150},
    {'id':20, 'name': 'Cucumber Mint Cooler', 'price':150},
    {'id':21, 'name': 'Pink lemonade', 'price':170},
    {'id':22, 'name': 'Chilli guava', 'price':180},
    {'id':23, 'name': 'Energy sunrise', 'price':180},
    {'id':24, 'name': 'Classic Hot Chocolate', 'price':180},
    {'id':25, 'name': 'Dark Hot Chocolate', 'price':200},
    {'id':26, 'name': 'Hazelnut Hot Chocolate', 'price':220},
    {'id':27, 'name': 'Coca cola can', 'price':40},
    {'id':28, 'name': 'Sprite can', 'price':40},
    {'id':29, 'name': 'Fanta can', 'price':40},
    {'id':30, 'name': 'Diet Coke can', 'price':40},
    {'id':31, 'name': 'Diet Sprite can', 'price':40},
    {'id':32, 'name': 'Redbull can', 'price':150},
    {'id':33, 'name': 'Monster energy can', 'price':120},
    {'id':34, 'name': 'Water Bottle', 'price':20},
    {'id':35, 'name': 'Veg. Cheese Sandwich', 'price':150},
    {'id':36, 'name': 'Potato veg. wrap', 'price':120},
    {'id':37, 'name': 'Alfredo pasta', 'price':180},
    {'id':38, 'name': 'Pink sauce pasta', 'price':200},
    {'id':39, 'name': 'Aloo patty burger', 'price':80},
    {'id':40, 'name': 'Tandoori paneer Burger', 'price':90},
    {'id':41, 'name': 'Cheeseburger', 'price':90},
    {'id':42, 'name': 'Cheese garlic bread', 'price':100},
    {'id':43, 'name': 'Salted fries', 'price':80},
    {'id':44, 'name': 'Peri Peri fries', 'price':90},
    {'id':45, 'name': 'Cheesy fries', 'price':100},
    {'id':46, 'name': 'Classic NewYork cheesecake', 'price':150},
    {'id':47, 'name': 'Blueberry Cheesecake', 'price':170},
    {'id':48, 'name': 'Nutella cheesecake', 'price':170},
    {'id':49, 'name': 'Biscoff Cheesecake', 'price':170},
    {'id':50, 'name': 'Chocolate cupcake', 'price':70},
    {'id':51, 'name': 'Vanilla cupcake', 'price':70},
    {'id':52, 'name': 'Chocolate pastry', 'price':100},
    {'id':53, 'name': 'Vanilla pastry', 'price':100},
    {'id':54, 'name': 'Brownie', 'price':100},
    {'id':55, 'name': 'Waffle sandwich', 'price':150},
    {'id':56, 'name': 'Pancakes', 'price':120},
    {'id':57, 'name': 'Donut', 'price':70},
    {'id':58, 'name': 'Pound cake piece', 'price':100},
    {'id':59, 'name': 'Icecream(scoop)', 'price':70},
    {'id':60, 'name': 'Icecream(sundae)', 'price':150},
]

#main programs:
# ---------------------------------------------------

#1. View menu:
def viewmenu():
    drinks='Drinks'
    snacks='Snacks'
    desserts='Desserts'
    print('-'*50)
    print('Menu')
    print('-'*50)
    print('ID \t NAME \t \t \t \t Price')
    print('-'*50)
    print(drinks.center(30,'-'))
    print('Coffees')
    for dish in menu[0:5]:
        print(f'{dish.get('id'):<5} {dish.get('name'):<25} {dish.get('price'):>10}')
    print('~--~--~')
    print('Tea')
    for dish in menu[5:8]:
        print(f'{dish.get('id'):<5} {dish.get('name'):<25} {dish.get('price'):>10}')
    print('~--~--~')
    print('Shakes')
    for dish in menu[8:15]:
        print(f'{dish.get('id'):<5} {dish.get('name'):<25} {dish.get('price'):>10}')
    print('~--~--~')
    print('Mocktails')
    for dish in menu[15:23]:
        print(f'{dish.get('id'):<5} {dish.get('name'):<25} {dish.get('price'):>10}')
    print('~--~--~')
    print('Hot Chocolate')
    for dish in menu[23:26]:
        print(f'{dish.get('id'):<5} {dish.get('name'):<25} {dish.get('price'):>10}')
    print('~--~--~')
    print('Other Drinks')
    for dish in menu[26:34]:
        print(f'{dish.get('id'):<5} {dish.get('name'):<25} {dish.get('price'):>10}')
    
    #-----
    print('~--~--~')
    print(snacks.center(30,'-'))
    for dish in menu[34:45]:
        print(f'{dish.get('id'):<5} {dish.get('name'):<25} {dish.get('price'):>10}')
    
    #-----
    print('~--~--~')
    print(desserts.center(30,'-'))
    print('~--~--~')
    print('Cheesecakes')
    for dish in menu[45:49]:
        print(f'{dish.get('id'):<5} {dish.get('name'):<25} {dish.get('price'):>10}')
    print('~--~--~')
    print('Others')
    for dish in menu[49:58]:
        print(f'{dish.get('id'):<5} {dish.get('name'):<25} {dish.get('price'):>10}')
    print('~--~--~')
    print('Icecream')
    for dish in menu[58:60]:
        print(f'{dish.get('id'):<5} {dish.get('name'):<25} {dish.get('price'):>10}')
    print(main_function())


#2. Add item
order_list=[]
def add_item():
    print('Which item would you like to add?')
    x= int(input('Enter dish ID : '))
    print(x)
    for item in menu:
        if item not in order_list:
            if item['id']==x:
                order_list.append(item)
                item['qty']=1
                print(f'{item['name']} added to cart.')
                print('-'*50)
                break
        else:
            if item['id']==x:
                item['qty'] += 1
                print(f'{item['name']} added to cart.')
                print('-'*50)
                break
    print(main_function())

#3. Remove item
order_list=[]
def remove_item():
    print('Which item would you like to remove?')
    x= int(input('Enter dish ID : '))
    print(x)
    for item in menu:
        if item not in order_list:
            if item['id']==x:
                order_list.pop(item)
                item['qty']=1
                print(f'{item['name']} removed from cart.')
                print('-'*50)
                break
        else:
            if item['id']==x:
                item['qty'] -= 1
                print(f'{item['name']} removed from cart.')
                print('-'*50)
                break
    print(main_function())

#Item total price
item_totalprice=0
def itemtotalprice():
    item_totalprice =sum(item['price'] for item in order_list)
    print(item_totalprice)

#4. View Cart
def view_cart():
    print('Here is your cart:')
    print('-'*23+'CART'+'-'*23)
    print('ID \t NAME \t \t \t Qty. \t   Price')
    print('-'*50)
    for cartitem in order_list:
        print(f'{cartitem.get('id'):<5} {cartitem.get('name'):<28} {cartitem.get('qty'):<5} Rs{cartitem.get('price'):>5}')
    print('-'*50)
    item_totalprice = 0
    for item in order_list:
        item_totalprice= item_totalprice + (item.get('qty')*item.get('price'))
    print(f'Sub Total : \t \t \t \t Rs{item_totalprice}')
    print(main_function())


#5. Finish order
def finish_order():
    print('Order received!')
    print('Your order will be prepared soon.')
    print(get_bill)
    print('*'*50)
    ('Thank you for visiting. See you later and visit again :)')


#6. Get bill
def get_bill():
    print('Here is your bill:')
    print('-'*42)
    print("LEMON'S CAFE")
    print('-'*19+'BILL'+'-'*19)
    print('Qty. \t NAME \t \t \t  Price')
    print('-'*42)
    for cartitem in order_list:
        print(f'{cartitem.get('qty'):<5} {cartitem.get('name'):<25} Rs{cartitem.get('price'):>5}')
    print('-'*42)
    item_totalprice = 0
    for item in order_list:
        item_totalprice= item_totalprice + (item.get('qty')*item.get('price'))
    print(f'Subtotal: \t\t\t Rs{item_totalprice}')
    tax = float(0.09*item_totalprice)
    print(f'GST tax: \t\t\t Rs{tax}')
    grand_total= float(item_totalprice+tax)
    print('-'*42)
    print(f'Grand Total: \t\t\t Rs{grand_total}')
    print('-'*42)
    print('Have a good day!')

#greet function  
def main_function():
    user_i1= int(input("What would you like to do: \n 1)View Menu \n 2)Add Item \n 3)Remove item \n4)View Cart \n5)Finish order \nEnter your response : "))
    if actions['view menu']==user_i1:
        print(viewmenu())
    elif actions['add item']==user_i1:
        print(add_item())
    elif actions['view cart']==user_i1:
        print(view_cart())
    elif actions['remove item']==user_i1:
        print(remove_item())
    elif actions['finish order']==user_i1:
        print(finish_order())
    else:
        print('See you later. Have a good day!')

#greet main
print('-'*30)
print('-'*30)
print("LEMON'S CAFE")
print('-'*30)
print('-'*30)
print(main_function())





