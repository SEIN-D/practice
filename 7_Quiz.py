# Quiz) 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서: 
# 이름: 
# 업무 요약: 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건: 파일명은 ‘1주차.txt’, ‘2주차.txt’, ... 와 같이 만듭니다.

for i in range(1,51):
    with open("Week {0}.txt".format(i), "w", encoding="utf8") as report:
        report.write("- Weekly Report: Week {0} -".format(i))
        report.write("Department: ")
        report.write("Name: ")
        report.write("Work Summary: ")
