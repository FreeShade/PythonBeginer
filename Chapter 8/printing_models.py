# допоміжний файл з функціями для тренування імпорту


def print_models(unprinted_designs, completed_models):
    """
    Симулювати друк кожного креслення, доки всі не закінчаться.
    Перенести кожен малюнок до completed_models після друку.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Показати всі надруковані моделі."""
    print("\nThe following models have been printed.")
    for completed_model in completed_models:
        print(completed_model)
