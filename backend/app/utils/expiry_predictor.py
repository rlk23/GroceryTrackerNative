from datetime import datetime, timedelta
from typing import Dict, Optional


# Expiry rules based on category
EXPIRY_RULES: Dict[str, int] = {
    # Dairy
    "milk": 7,
    "cheese": 14,
    "yogurt": 7,
    "butter": 14,
    "dairy": 7,
    
    # Meat & Seafood
    "meat": 3,
    "beef": 3,
    "pork": 3,
    "chicken": 3,
    "fish": 2,
    "seafood": 2,
    
    # Produce
    "vegetables": 5,
    "fruits": 7,
    "lettuce": 5,
    "tomatoes": 7,
    "bananas": 5,
    "apples": 14,
    
    # Bakery
    "bread": 5,
    "bakery": 5,
    
    # Pantry
    "canned": 365,
    "pasta": 365,
    "rice": 365,
    "pantry": 365,
    
    # Beverages
    "juice": 7,
    "soda": 180,
    "beverages": 30,
    
    # Frozen
    "frozen": 90,
    
    # Other
    "other": 7,
}


def predict_expiry_date(name: str, category: str, purchase_date: Optional[datetime] = None) -> datetime:
    """
    Predict expiry date based on item name and category.
    
    Args:
        name: Item name (used for specific matching)
        category: Item category
        purchase_date: Date of purchase (defaults to now)
    
    Returns:
        Predicted expiry date
    """
    if purchase_date is None:
        purchase_date = datetime.now()
    
    # Normalize inputs
    name_lower = name.lower()
    category_lower = category.lower()
    
    # Check for specific product matches first
    days = None
    for key, days_to_expire in EXPIRY_RULES.items():
        if key in name_lower or key in category_lower:
            days = days_to_expire
            break
    
    # Default to 7 days if no match found
    if days is None:
        days = 7
    
    return purchase_date + timedelta(days=days)


def get_expiry_days(name: str, category: str) -> int:
    """
    Get the number of days until expiry for a given item.
    
    Args:
        name: Item name
        category: Item category
    
    Returns:
        Number of days until expiry
    """
    name_lower = name.lower()
    category_lower = category.lower()
    
    for key, days in EXPIRY_RULES.items():
        if key in name_lower or key in category_lower:
            return days
    
    return 7  # Default

