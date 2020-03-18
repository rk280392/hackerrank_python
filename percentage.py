if __name__ == '__main__':
    n = int(input("Please enter number of students: "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Please enter your name and marks: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Please enter your name: ")
    query_average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(("{0:.2f}".format(query_average)))

