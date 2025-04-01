#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price
#(price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Applies discount only if it is 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price


#Using the calculate_discount function, prompt the user to enter the original price
#of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(price, discount_percent)
    
    # Print result
    print(f"Final price after applying discount: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numerical values for price and discount percentage.")
