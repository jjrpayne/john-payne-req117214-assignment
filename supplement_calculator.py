def calculate(in_data):
    id = in_data['id']
    is_eligible = in_data['familyUnitInPayForDecember']
    if in_data['familyComposition'] not in ('single', 'couple'):
        raise Exception("Invalid familyComposition value")
    if is_eligible:
        if in_data['familyComposition'] == 'single':
            base_amount = 60.0
        else:
            base_amount = 120.0
        children_amount = in_data['numberOfChildren'] * 20.0
        supplement_amount = base_amount + children_amount
    else:
        base_amount = children_amount = supplement_amount = 0.0

    return {
        'id': id,
        'isEligible': is_eligible,
        'baseAmount': base_amount,
        'childrenAmount': children_amount,
        'supplementAmount': supplement_amount
    }