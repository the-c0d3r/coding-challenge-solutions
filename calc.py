while True:
    print(''.join(["[%s]>>%s\n"%(k,v) for k,v in {1:"Addition",2:"Subtraction",3:"Multiplication",4:"Division",5:"Quit"}.items()]))    
    choice = (lambda x: x if x in range(5) else exit())(int(input("Enter choice : ")))
    cmdTable = {1:lambda x,y: x+y,2:lambda x,y: x-y,3:lambda x,y: x*y,4:lambda x,y: x/y}
    print("Result : %d\n" % cmdTable[choice](int(input("Number 1 : ")),int(input("Number 2 : "))))
    # print("Result : %d\n" % cmdTable[choice(int(input("Enter choice : ")))](int(input("Number 1 : ")),int(input("Number 2 : "))))

# while 1:
#     print(''.join("[%s]>>%s\n"%(i+1,v)for i,v in enumerate(["Addition","Subtraction","Multiplication","Division","Quit"])))    
#     c=lambda x:x*(0<x<5)or exit()
#     n="Number %d : ";q=input;h=c(int(q("Enter choice : ")))-1;print("Result : %d\n"%eval(q(n%1)+"+-*/"[h]+q(n%2)))