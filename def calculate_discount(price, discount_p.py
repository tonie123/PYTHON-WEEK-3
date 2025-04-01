def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Parameters:
    price (float): The original price.
    discount_percent (float): The discount percentage.

    Returns:
    float: The final price after applying the discount if it's 20% or higher,
           otherwise returns the original price.
    """
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    return price

# Get user input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Display result
if discount_percent >= 20:
    print(f"Final price after discount: {final_price:.2f}")
else:
    print(f"No discount applied. Original price: {price:.2f}")