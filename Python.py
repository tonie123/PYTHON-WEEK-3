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

# Example usage:
print(calculate_discount(100, 25))  # Output: 75.0
print(calculate_discount(100, 15))  # Output: 100.0