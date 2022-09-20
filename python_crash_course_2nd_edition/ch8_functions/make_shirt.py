def make_shirt(size="large", text="I love Python"):
    """Display the size of the shirt and the message that will be on the shirt"""
    print(f"shirt size requested is {size.lower()} and message on the shirt is '{text}'")

make_shirt("medium", "I hate cats!")
make_shirt(size="medium", text="I hate cats!")

make_shirt()
make_shirt(size="medium")
