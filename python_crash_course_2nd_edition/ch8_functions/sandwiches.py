def sandwich(*toppings):
    """list of items a person wants on a sandwich"""
    print(f"\nsomeone wants the following on their sandwich:")
    for t in toppings:
        print(f"- {t}")


sandwich("ham", "pineapple")
sandwich("swiss", "turkey")
