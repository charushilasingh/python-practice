# TinyHouse Shop Web Chat BOt
# Greeting
from unicodedata import category


def greeting():
    name = input(
        "thanks for contacting Tiny House. May I have your name:?"
    ).capitalize()
    print(f"Thanks, {name}")
    return

    # Inquiry category


def select_category():
    category = input(
        "Please select from one of the categories below using the numbers 1 - 5. [1] Store Hours and locations [2] Status of Order [3] Issue with order [4] Design servises [5] Other"
    )
    if category == "1":
        store_location_hours()
        return

    if category == "2":
        order_status()
        return

    if category == "3":
        order_issue()
        return
    if category == "4":
        design_services()
        return
    if category == "5":
        other()
        return

    if category not in ["1", "2", "3", "4", "5"]:
        select_category()


# category: Store Location  and  hours
def store_location_hours():
    location = "2300 Riverdale Lane Boston, Ma 02101"
    hours = "Monday - saturday From 10 am to 6 PM"
    print(f"Tiny space is located at {location}. the space is open {hours}.")
    additional_question = input("May I help you win anythimg else? (Yes/No)").lower()
    if additional_question == "yes":
        select_category()
    elif additional_question == "no":
        print("thanks for containing Tiny Space")
    return


# Category: Status of order
def order_status():
    print("Sure,I can help you with that.")
    full_name = input("May I have the full name on the order?")
    order_number = input("May I have the order number?")
    transfer_Elliot()
    return


# category: Issue with order
def order_issue():
    print("I'm sorry that you are rxpercing issues with your order.")
    full_name = input("May i have the full name on the order?")
    order_number = input("May I have the order number?")
    issue = "Could you please describe the issue with your order:?"
    transfer_chrissa()
    return


# category: Design Services
def design_services():
    print("I can definitely help you out with your design questions:")
    transfer_ramon()
    return


# category : other
def other():
    transfer_Trinity()
    return


# Transfers to tiny space online team
def transfer_Elliot():
    print("awesome! I'm checking the status of the order now.")
    return


def transfer_chrissa():
    print("Thanks for providing that information. i'm looking into this now.")
    return


def transfer_ramon():
    design_question = input("Tell me how I may be of assistance.")
    return


def transfer_Trinity():
    other_inquiry = input(
        "No problem, please describe to me how I may be of assistance."
    )
    return


# call the functions to start the chat bot
greeting()
select_category()
