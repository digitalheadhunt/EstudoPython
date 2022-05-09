def ip_validation(str):
    splited_ip = str.split(".")
    if len(splited_ip) < 4 or len(splited_ip) > 4 :
        return False
    for x in splited_ip:
        if x.startswith('0') and len(x) > 1:
            return False
    new = [True for x in splited_ip if x.isdigit() and int(x) >= 0 and int(x) <= 255]
    result = True if len(new) == len(splited_ip) else False
    print(splited_ip,new)
    return result


print(ip_validation('230.029.222.176'))

