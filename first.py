# Introduction & Asking For Order"
intro =  '''
Hi And Welcome To Austins Pizzeria!
Please note our menu options have changed:

Our Current Menu:
One: Slice Of Pizza + A Drink $13.95
Two: Penne Al Vodka + A Drink $12.95
Three: Tuscany Grilled Pasta + A Drink $17.95

Please Make A Selection

'''
print(intro)



#Dict For Orders
orders = {
"One": {"item": "Slice Of Pizza", "price": 1.95},
"Two": {"item": "Pesto Pasta", "price": 19.65},
"Three": {"item": "Spaghetti", "price": 15.90}
 }

#Dict For Available Cards
cards = {
"Capital One": {"card": "Capital One XX34", "balance": 2101.00},
"American Express": {"card": "American Express XX34", "balance": 1141.20},
}


# Get Users Order Selection
selection = input("Please type the number of which you would like to order ")


#Main Loop
while True:

    # Essentially, if the selection the user made is in the said dictionary, we will assign
    # the price and item name to a variable that can later be displayed
    if selection in orders:
        selected_item = orders[selection]["item"]
        selected_price = orders[selection]["price"]

        print(" \nNice Choice! We Will Have That", selected_item, "Coming Right Up")

        #Payment Section
        pay = input("\nIn the mean time would you like to pay? : ")
        if pay == "Yes":
            print("\nPerfecto thata willa be,", selected_price)
        if pay == "No":
            print("Get outtah my storah beforah iah calla daa coppas")
            break

        #Display Cards
        cardsdisplay = '''
        \nTime To Check Your Wallet...
        You Have:
        "Capital One"
        "American Express"
        '''
        print(cardsdisplay)

        #Variable for holding the input for which card should be used
        card_selection = input("What Card Would You Like To Use: ")

        # An if statment checking to see if the selected card is in the cards dic,
        # If it is, we will subtract the price from the balance and assign the remaining amount to a variable
        if card_selection in cards:
         remain = cards[card_selection]["balance"] - orders[selection]["price"]

         print("\nYour remaining balance is ", remain)
         print("\nThank you for your payment")
         break

        # Failsafe for entering wrong card
        else:
            print("No such card found")
            break


        #If not a good option, no longer a vaild option
    else:
        print("Not a vaild option")
        break






