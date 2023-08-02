a = 55
match a:
    case 0:
        print("Zero")
    case 5:
        print("its 5")
    case _ if a!=10:
        print("a is not 10")
    case _ if a!=2:
        print("a is not 20")
    case _ :
        print("a")
        
      