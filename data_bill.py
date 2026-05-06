# constant values are set here:
TIER_1_DATA_LIMIT_GB = 10
TIER_2_DATA_LIMIT_GB = 20
PREMIUM_USER_OVERAGE_RATE_TIER_2 = 1
REGULAR_USER_OVERAGE_RATE_TIER_2 = 2
PREMIUM_USER_OVERAGE_RATE_TIER_3 = 2
REGULAR_USER_OVERAGE_RATE_TIER_3 = 3
FINAL_OVERAGE_COST = 0

# Your code goes here:
user_data = float(input("Please enter the data you have used (GB): "))
base_plan_cost = float(input("Please enter your base monthly plan cost: "))
has_premium = input("Do you have a premium plan? (yes/no): ") == "yes"

overage_data = user_data - TIER_1_DATA_LIMIT_GB