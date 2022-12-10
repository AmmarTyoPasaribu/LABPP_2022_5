import re

ipv4 = r"(([01]?[0-9]?[0-9]|2[0-4][0-9]|2[5][0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|2[5][0-5])"
ipv6 = "([0-9]|[a-zA-Z]){1,4}:([0-9]|[a-zA-Z]){1,4}:([0-9]|[a-zA-Z]){1,4}:([0-9]|[a-zA-Z]){1,4}:([0-9]|[a-zA-Z]){1,4}:([0-9]|[a-zA-Z]){1,4}:([0-9]|[a-zA-Z]){1,4}:([0-9]|[a-zA-Z]){1,4}"

N_baris = int(input())
N_result = []

for i in range(N_baris):
    x = input()

    check_ipv4 = re.search(ipv4, x)
    check_ipv6 = re.search(ipv6, x)

    if check_ipv4 != None:
        if check_ipv4.span() == (0,len(x)):
            N_result += ["IPv4"]
        else:
            N_result += ["Bukan IP Address"]
    if check_ipv6 != None:
        if check_ipv6.span() == (0,len(x)):
            N_result += ["IPv6"]
        else:
            N_result += ["Bukan IP Address"]
    if check_ipv4 == None and check_ipv6 == None:
        N_result += ["Bukan IP Address"]

for i in N_result:
    print(i)