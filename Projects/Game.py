import random  # Ye Python ka ek tool hai jo random number sochne me madad karta hai

secret_number = random.randint(1, 100) # Computer 1 se 100 ke beech ek number chunta hai
attempts = 0  # Ye count karega ki aapne kitni baar guess kiya

print("Welcome to the Number Guessing Game!")
print("Maine 1 se 100 ke beech ek number socha hai. Chalo guess karo!")

while True:
    # User se unka guess pucho
    guess = int(input("Apna guess enter karo: "))
    attempts = attempts + 1

    # Hints check karne ke liye if/elif/else ka use
    if guess < secret_number:
        print("Nahi, ye thoda chhota hai! Bada number try karo. ⬆️")
    elif guess > secret_number:
        print("Nahi, ye thoda bada hai! Chhota number try karo. ⬇️")
    else:
        # Jab guess aur secret_number barabar ho jayein!
        print("🎉 Badhai ho! Aapne bilkul sahi guess kiya!")
        print("Aapne", attempts, "attempts mein game jeet liya.")
        break  # Game khatam, isliye loop se bahar nikal jao