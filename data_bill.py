# constant values are set here:
TIER_1_DATA_LIMIT_GB = 10
TIER_2_DATA_LIMIT_GB = 20
PREMIUM_USER_OVERAGE_RATE_TIER_2 = 1
REGULAR_USER_OVERAGE_RATE_TIER_2 = 2
PREMIUM_USER_OVERAGE_RATE_TIER_3 = 2
REGULAR_USER_OVERAGE_RATE_TIER_3 = 3
final_overage_cost = 0

# Your code goes here:
user_data = float(input("Please enter the data you have used (GB): "))
base_plan_cost = float(input("Please enter your base monthly plan cost: "))
has_premium = input("Do you have a premium plan? (yes/no): ") == "yes"

overage_data = user_data - TIER_1_DATA_LIMIT_GB

if user_data <= TIER_1_DATA_LIMIT_GB:
    final_overage_cost = final_overage_cost
elif user_data > TIER_1_DATA_LIMIT_GB and user_data <= TIER_2_DATA_LIMIT_GB:
    if has_premium:
        final_overage_cost = PREMIUM_USER_OVERAGE_RATE_TIER_2 * overage_data
    else:
        final_overage_cost = REGULAR_USER_OVERAGE_RATE_TIER_2 * overage_data
else:
    if has_premium:
        final_overage_cost = PREMIUM_USER_OVERAGE_RATE_TIER_3 * overage_data
    else:
        final_overage_cost = REGULAR_USER_OVERAGE_RATE_TIER_3 * overage_data

total_cost = base_plan_cost + final_overage_cost

if user_data > 10:
    print(f"\nYou are {overage_data:.2f} GB over your data limit.")
else:
    print("You are within your data limit.")

print(f"Overage Cost: ${final_overage_cost:.2f}")
print(f"Total Bill: ${total_cost}")

