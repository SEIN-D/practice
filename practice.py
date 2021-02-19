for i in range(1,51):
    with open("Week {0}.txt".format(i), "w", encoding="utf8") as report:
        report.write("- Weekly Report: Week {0} -".format(i))
        report.write("Department: ")
        report.write("Name: ")
        report.write("Work Summary: ")
