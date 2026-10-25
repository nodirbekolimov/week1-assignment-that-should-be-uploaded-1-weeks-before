# Grocery Store Checkout System
# Uses only concepts from the course notes:
# variables, input(), type conversion, operators, booleans, f-strings

# ---------- Item input ----------
item1_name = input("Item 1 name: ")
item1_price = float(input("Item 1 price (sum): "))
item1_qty = int(input("Item 1 quantity: "))

item2_name = input("Item 2 name: ")
item2_price = float(input("Item 2 price (sum): "))
item2_qty = int(input("Item 2 quantity: "))

item3_name = input("Item 3 name: ")
item3_price = float(input("Item 3 price (sum): "))
item3_qty = int(input("Item 3 quantity: "))

# ---------- Customer input ----------
customer_name = input("Customer name: ")
has_loyalty_card = input("Has loyalty card? (yes/no): ") == "yes"
is_senior_citizen = input("Is senior citizen? (yes/no): ") == "yes"
day_of_week = int(input("Day of week (1=Monday ... 7=Sunday): "))

# ---------- Item totals and subtotal ----------
item1_total = item1_price * item1_qty
item2_total = item2_price * item2_qty
item3_total = item3_price * item3_qty
subtotal = item1_total + item2_total + item3_total

# ---------- Eligibility (booleans) ----------
loyalty = has_loyalty_card
senior = is_senior_citizen
weekend = day_of_week >= 6
large_purchase = subtotal >= 300000

# ---------- Discount amounts (0 if not eligible) ----------
loyalty_amount = loyalty * subtotal * 0.08
senior_amount = senior * subtotal * 0.12
weekend_amount = weekend * subtotal * 0.15
large_amount = large_purchase * subtotal * 0.05

# ---------- Choose the best main discount (boolean arithmetic) ----------
pick_loyalty = loyalty and (loyalty_amount >= senior_amount and loyalty_amount >= weekend_amount)
pick_senior = senior and (senior_amount > loyalty_amount and senior_amount >= weekend_amount)
pick_weekend = weekend and (weekend_amount > loyalty_amount and weekend_amount > senior_amount)

main_discount = (pick_loyalty * loyalty_amount
                 + pick_senior * senior_amount
                 + pick_weekend * weekend_amount)

# Large purchase discount stacks with the main discount
total_discounts = main_discount + large_amount

# ---------- Bag fee ----------
bag_fee_applied = subtotal < 100000
bag_fee = (subtotal < 100000) * 5000

# ---------- Subtotal after discounts and fees ----------
subtotal_after_discounts = subtotal - total_discounts + bag_fee

# ---------- Tax and parking ----------
tax = subtotal_after_discounts * 0.15
free_parking = subtotal_after_discounts >= 250000
parking = (subtotal_after_discounts < 250000) * 10000

# ---------- Final total and net savings ----------
final_total = subtotal_after_discounts + tax + parking
net_savings = total_discounts - bag_fee - parking

# ---------- Receipt ----------
print(f"\n\n{'=' * 60}")
print("GROCERY STORE RECEIPT")
print(f"{'=' * 60}")
print(f"Customer: {customer_name}")
print(f"Loyalty card: {has_loyalty_card}")
print(f"Senior citizen: {is_senior_citizen}")
print(f"Day of week: {day_of_week}")

print(f"\n{'-' * 60}")
print("Items (item, quantity, price, total):")
print(f"{item1_name}, {item1_qty}, {item1_price:.2f}, {item1_total:.2f}")
print(f"{item2_name}, {item2_qty}, {item2_price:.2f}, {item2_total:.2f}")
print(f"{item3_name}, {item3_qty}, {item3_price:.2f}, {item3_total:.2f}")
print(f"{'-' * 60}")
print(f"Subtotal before discounts: {subtotal:.2f} sum")

print("\n--- Discounts ---")
print(f"Loyalty discount - eligible: {loyalty}, amount: {loyalty_amount:.2f} sum")
print(f"Senior discount - eligible: {senior}, amount: {senior_amount:.2f} sum")
print(f"Weekend special - eligible: {weekend}, amount: {weekend_amount:.2f} sum")
print("Main discount selected:")
print(f"  Loyalty applied: {bool(pick_loyalty)}")
print(f"  Senior applied: {bool(pick_senior)}")
print(f"  Weekend applied: {bool(pick_weekend)}")
print(f"  Main discount amount: {main_discount:.2f} sum")
print(f"Large purchase - eligible: {large_purchase}, amount: {large_amount:.2f} sum")
print(f"Total discounts applied: {total_discounts:.2f} sum")

print("\n--- Fees ---")
print(f"Bag fee applied: {bag_fee_applied}, amount: {bag_fee:.2f} sum")
print(f"Subtotal after discounts and fees: {subtotal_after_discounts:.2f} sum")
print(f"Tax (15%): {tax:.2f} sum")
print(f"Free parking: {free_parking}, parking fee: {parking:.2f} sum")

print(f"{'=' * 60}")
print(f"FINAL TOTAL: {final_total:.2f} sum")
print(f"{'=' * 60}")
print(f"Net savings (negative = extra fees): {net_savings:.2f} sum")
print(f"{'=' * 60}\n\n")
