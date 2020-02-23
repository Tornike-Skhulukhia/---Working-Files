
# 100    - A - 4  - 6    - 
# 82     - B - 3  - 6    - 
# 75     - C - 2  - 6    - 
# 100    - A - 4  - 6    - 

# (4 * 6 + 3 * 6 + 2 * 6 + 4 * 6) / (6 * 4) = 
# (4 + 3 + 2 + 4) /  4 = 3.25



def calculate_gpa(raw_scores):
    '''
    calculates GPA using given list of grades

    arguments:
        1.raw_scores - list of integers
    '''

    # raw_scores = [100, 82, 75, 100]
    scaled_scores  = []

    for score in raw_scores:
        # A  '97'
        if 91 <= score <= 100:
            scaled_score = 4
        # B
        elif 81 <= score <= 90:
            scaled_score = 3
        # C
        elif 71 <= score <= 80:
            scaled_score = 2
        # D
        elif 61 <= score <= 70:
            scaled_score = 1
        else:
            scaled_score = 0

        scaled_scores.append(scaled_score)

    GPA = sum(scaled_scores) / len(scaled_scores)
    # print(GPA)
    return GPA


 
