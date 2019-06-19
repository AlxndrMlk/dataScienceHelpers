def replace_decimal(x, old_sep=',', new_sep='.'):
    try:
        x = x.replace(old_sep, new_sep)
        return float(x)
    except (TypeError, ValueError, AttributeError) as e:
        pass
