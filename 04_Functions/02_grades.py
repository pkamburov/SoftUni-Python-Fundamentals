def convert_grade(grade):
    if grade <= 2.99:
        return "Fail"
    elif grade <= 3.49:
        return "Poor"
    elif grade <= 4.49:
        return "Good"
    elif grade <= 5.49:
        return "Very Good"
    else:
        return "Excellent"

grade = float(input())

print(convert_grade(grade))
