def get_scores():
    scores = {}
    
    while True:
        name = input("name:")
        if name == "":
            break
        score = int(input("score:"))
        if name in scores:
            scores[name] += (score,)
        else:
            scores[name] = (score,)
    return scores        
        
def calc_average(scores):
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)
    return average
    
def calc_averages(scores):
    averages = {}
    for name,student_scores in scores.items():
        averages[name] = calc_average(student_scores)
    return averages
    
def sort_dict(dict):
    sorted_scores = {}
    for key in sorted(dict.keys()):
        sorted_scores[key] = dict[key]
    return sorted_scores    
    
scores = get_scores()
print(sort_dict(scores))
averages = calc_averages(scores)
print(sort_dict(averages))