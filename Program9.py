'''
Create a class bill. Bill should contain date, customer name and details of # 
of items - name,rate, quantity, total amount. Make a bill and display it.

'''

class Bill:

    def __init__(s,date,name,items):
        s.date = date
        s.name = name
        s.items = items

    def display_bill(s):
        print('--------------BILL----------------')
        print('Date: ' , s.date)
        print('Recipent: ', s.name)
        print('-----------------------------------')
        print("item \t rate \t quantity \t total")

        grandtotal = 0
        for item in s.items:
            name = item["name"]
            rate = item["rate"]
            quantity = item["quantity"]

            total = rate * quantity

            grandtotal += total

            print(f"{name:<5} \t {rate:<5} \t {quantity:<5} \t {total:<5}")
        
        print('-----------------------------------')
        print('Grand Total: ', grandtotal)
        print('-----------------------------------')

def main():

    for i in range(1,5) :
        date = '2023-01-01'
        name = 'Harry Bohora'
        items = [

    
            {"name": "a", "rate": 20, "quantity": 4,} ,
            {"name": "a", "rate": 20, "quantity": 4,} ,
            {"name": "a", "rate": 20, "quantity": 4,} ,
        ]

        bill = Bill(date,name,items)
        bill.display_bill()
    
main()