# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    total = sum(bill) - bill[k]
    if(total//2 == b ):
        print("Bon Appetit")
    else:
        print(b - total//2)
