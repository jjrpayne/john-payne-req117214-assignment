def calculate(in_data):
    id = in_data['id']
    is_eligible = in_data['familyUnitInPayForDecember']
    if not is_eligible:
        base_amount = children_amount = supplement_amount = 0.0
    else:
        if in_data['familyComposition'] == 'single':
            base_amount = 60.0
        elif in_data['familyComposition'] == 'couple':
            base_amount = 120.0
        else:
            raise Exception("Invalid familyComposition value")
        children_amount = in_data['numberOfChildren']*20.0
        supplement_amount = base_amount + children_amount

    return {
        'id': id,
        'isEligible': is_eligible,
        'baseAmount': base_amount,
        'childrenAmount': children_amount,
        'supplementAmount': supplement_amount
    }