def print_models(unprinted_designs, completed_models):
    """
    simulate printing each desing, until none are left
    move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """show all the models that were printed"""
    print(f"\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
