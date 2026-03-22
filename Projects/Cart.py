cart = []

print("Welcome to Digital Shopping Cart")

while True:
	print("\nChoose an option:")
	print("Press 1: Add item to cart")
	print("Press 2: Remove item from cart")
	print("Press 3: View cart and total item count")
	print("Press 4: Exit")

	choice = input("Enter your choice (1/2/3/4): ")

	if choice == "1":
		item_name = input("Enter item name to add: ").strip()
		if item_name:
			cart.append(item_name)
			print(f"'{item_name}' has been added to your cart.")
		else:
			print("Item name cannot be empty.")

	elif choice == "2":
		item_name = input("Enter item name to remove: ").strip()
		if item_name in cart:
			cart.remove(item_name)
			print(f"'{item_name}' has been removed from your cart.")
		else:
			print(f"'{item_name}' is not in your cart.")

	elif choice == "3":
		if cart:
			print("\nYour cart items are:")
			for index, item in enumerate(cart, start=1):
				print(f"{index}. {item}")
		else:
			print("\nYour cart is empty.")

		print(f"Total items in cart: {len(cart)}")

	elif choice == "4":
		print("Thank you for using Digital Shopping Cart. Goodbye!")
		break

	else:
		print("Invalid choice. Please enter 1, 2, 3, or 4.")
