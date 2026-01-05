def ortacha_baho(baholar):
    if not baholar:
        return 0
    return sum(baholar) / len(baholar)

def eng_yuqori_baho(baholar):
    if not baholar:
        return None
    return max(baholar)

def eng_past_baho(baholar):
    if not baholar:
        return None
    return min(baholar)
