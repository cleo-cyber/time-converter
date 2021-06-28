problems=["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
if len(problems)>5:
    print("error too many problems")
for problem in problems:
    problem=problem.split()
    if problem[1] in "+":
        problem[1]="+"
    elif problem[1] in "-":
        problem[1]="-"
    else:
        print("Error operator must be '+' or '-'")
    try:
        value_1=int(problem[0])
        value_2=int(problem[2])
    except ValueError:
        print("Error number must only contain digits")
    if len(problem[0])>4 or len(problem[2])>4:
        print("Error: number cannot contan more than four digits")
    longest_op=max(len(problem[0]),len(problem[2]))
    width=longest_op +2
    output=f"{problem[0]:>{width}}\n {f'{problem[1]} {problem[2]}':>{width}}\n{'-'*width}"
    print("This is output")
    print(output)
    print("This is temp")
    temp=f"""
    {problem[0]}
    {problem[1]} {problem[2]}
    _____

"""
    print(temp)



