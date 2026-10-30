from .entities import guinea_pig, swiss_government

def main() -> None:
    bob = guinea_pig("Bob", 5, True, True)
    john = guinea_pig("John", 6, True, False)
    alex = guinea_pig("Oleksandr", 4, False, True)
    robert = guinea_pig("Robert", 2, False, False)

    gov = swiss_government()

    bob.eat()
    john.spend_time()
    alex.spend_time()
    robert.eat()

    gov.check_guinea_pig(bob)
    gov.check_guinea_pig(john)
    gov.check_guinea_pig(alex)
    gov.check_guinea_pig(robert)

if __name__ == "__main__":
    main()
