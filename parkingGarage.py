# Start Your Code here
class Garage():

    def takeTicket(tickets, parkingSpaces):

        if len(tickets) == 0:
            print("Sorry, garage full!")
        else:
            print(
                f"Here is your ticket number '{tickets.pop()}'\nYour parking spot is '{parkingSpaces.pop()}'")

    def payForParking(tickets, parkingSpaces):

        pay_park = input('Would you like to pay? yes/no')

        if pay_park.lower() == 'yes':
            Garage.leaveGarage(tickets, parkingSpaces)
        elif pay_park.lower() == 'no':
            print('Have a nice day!')
        else:
            return

    def leaveGarage(tickets, parkingSpaces):

        paid = input("Have you paid your ticket? yes/no")

        if len(tickets) == 9:
            print('Ticket already paid for!')
            return

        if paid.lower() == 'yes':
            tickets.append(tickets[-1]+1)
            parkingSpaces.append(parkingSpaces[-1]+1)
            print("Ticket paid.\nHave a nice day!")
        elif paid.lower() == 'no':
            print('Please pay for parking')
            Garage.payForParking(tickets, parkingSpaces)
        else:
            return


def run():

    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while True:

        welcome = input(
            'Welcome to garage! What would like to do? Take ticket (t) Pay ticket (p) Quit (q)')

        if welcome.lower() == 't':
            Garage.takeTicket(tickets, parkingSpaces)
        elif welcome.lower() == 'p':
            Garage.payForParking(tickets, parkingSpaces)
        elif welcome.lower() == 'q':
            print('Thanks for coming!')
            break


run()
