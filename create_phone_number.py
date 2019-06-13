def create_phone_number(n):
    new_n = [str(a) for a in n]
    l1 = new_n[:3]
    l1.insert(0,"(")
    l1.append(")")
    l2 = new_n[3:6]
    l2.append("-")
    l3 = new_n[6:]
    result = "".join(l1)+" "+"".join(l2)+"".join(l3)
    return result


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])