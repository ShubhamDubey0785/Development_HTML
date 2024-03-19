#take input from three users and find young,youngest and oldest
man1=int(input("put first man"))
man2=int(input("put second man"))
man3=int(input("put third man"))
if man1>man2 and man1>man3:
    print("man1 oldest")
elif man1>man2 and man1<man3:
    print("man1 young")
elif man1<man2 and man1<man3:
    print("man1 youngest")
elif man2>man1 and man2>man3:
    print("man2 oldest")
elif man2>man1 and man2<man3:
    print("man2 young")
elif man2<man1 and man2<man3:
    print("man2 youngest")
elif man3>man1 and man3>man2:
    print("man3 oldest")
elif man3<man1 and man3<man2:
    print("man3 youngest")
elif man3>man1 and man3<man2:
    print("man3 young")