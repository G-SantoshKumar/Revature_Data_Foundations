def highest_scorer(scores):
    highest = 0
    for name, score in scores.items():
        if score > highest:
            highest = score
    return name, score


scores = {"Ram":90, "Sham":79, "Mohan":98}

print(highest_scorer(scores))