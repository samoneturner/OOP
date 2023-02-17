import InsectClass as i


def main():
    # my_insect = i.Insect()

    mosquito = i.Insect("mosquito", 2, 4)
    housefly = i.Insect("housefly", 4, 8)

    mosquito.length_of_travel()
    housefly.length_of_travel()

    print(f"The {mosquito.get_type()} can fly up to {mosquito.get_travel()} miles")
    print(f"The {housefly.get_type()} can fly up to {housefly.get_travel()} miles")

    # print("This is the current insect:")
    # print("Wings: ", my_insect.get_wings())
    # print("Legs: ", my_insect.get_legs())
    # print("Flight: ", my_insect.get_travel())
    # print()

    # print("I am going to select 3 insects:")

    # for count in range(3):
    #     my_insect.length_of_travel()
    #     my_insect.insect_type()
    #     print("Wings: ", my_insect.get_wings())
    #     print("Legs: ", my_insect.get_legs())
    #     print("Flight: ", my_insect.get_travel())
    #     print("Type: ", my_insect.get_type())
    #     print()


main()
