def hanoi_solver(num):
    source = [i for i in range(num, 0, -1)]
    aux = []
    target = []
    initial_state = f"{source} {aux} {target}\n"
    return initial_state + hanoi_helper(num, source, target, aux , source, aux, target)
    

def hanoi_helper(num, source, target, aux, s_name, a_name, t_name):
    
    if num == 1:
        target.append(source[-1])
        source.pop()
        if source != [] or aux != []:
            return f"{s_name} {a_name} {t_name}\n"
        else:
            return f"{s_name} {a_name} {t_name}"
    step_1 = hanoi_helper(num-1, source, aux, target, s_name, a_name, t_name)

    target.append(source[-1])
    source.pop()
    step_2 = f"{s_name} {a_name} {t_name}\n"

    step_3 = hanoi_helper(num-1, aux, target, source, s_name, a_name, t_name)
    return step_1 + step_2 + step_3


if __name__ == '__main__':
    num = 3
    print(hanoi_solver(num))