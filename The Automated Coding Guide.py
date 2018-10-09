def PARSE(ab):
    if ab=='if':
        print('insert left and right operand:')
        a=input()
        b=input()
        print('insert operator')
        c=input()
        return ("if {} {} {}".format(a,c,b))

a=input()
print(PARSE(a))
