from math import log, sqrt

def punto_5(romano):
    valores={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    decimal=0
    print("a")
    if type(romano)==str:
        lista=list(romano.upper())
        for i in range(len(lista)):
            lista[i]=valores[lista[i]]
        mayorindex=lista.index(max(lista))
    if type(romano)==list:
        lista=romano
        mayorindex=lista.index(max(lista))
        print("b")
    for i in range(mayorindex):
        decimal-=lista[i]    
    for i in range (mayorindex,len(lista)):
        if lista[i]==lista[mayorindex]:
            decimal+=lista[i]
        else:
            break
        restaindex=i+1
    print(decimal)
    if len(lista)>restaindex:
        decimal+=punto_5(lista[restaindex:len(lista)])

    return decimal

def punto_6(char):
    if len(char)==1:
        return char
    else:
        return char[-1]+punto_6(char[0:(len(char)-1)])
    
def punto_7 (numero):
    if numero==1:
        return 1
    else:
        return (1/numero)+punto_7(numero-1)
    
def punto_8(decimal,lista=[],flag=1):
    neg=0
    if decimal<0:
        neg=1
        decimal*=-1
    lista.append(decimal%2)
    if decimal==0:
        return lista
    else:
        punto_8(decimal//2,lista,0)
    if flag==1:
        lista.pop()
        if neg==1:
            lista.append("-")
        lista.reverse()
        binario="".join(str(n)for n in lista)
        return binario

def punto_9(n,b,flag=0):
    if flag==0:
        return punto_9(n,b,1)+1
    elif flag==1:
        return log(n,b)
    
def punto_10(num=None,lista=[],cont=0):
    if cont==0:
        lista=list(str(num))
        print(lista)
        lista.pop()
        cont+=1
        punto_10(None,lista,cont)
        return lista[0]
    elif lista:
        lista.pop()
        cont+=1
        print(cont)
        punto_10(None,lista,cont)
    else:
        lista.append(cont)
        
def punto_11(num,lista=[],flag=0):
    inv=0
    neg=0
    if num==0:
        return 0
    elif num<0:
        num*=-1
        neg=1
        lista.append((num%10))
        num=num//10
    else:
        lista.append(num%10)
        num=num//10
    if num!=0:
        punto_11(num,lista,1)
    print(lista)
    if flag==0:
        for n in lista:
            inv=inv*10+n
            print(inv)
        if neg==1:
            inv*=-1
        return inv

def punto_12(num1,num2):
    if num1==num2:
        return num1
    elif num1<num2:
        return punto_12(num1,(num2-num1))
    else:
        return punto_12((num1-num2),num2)
    
def punto_13(num1,num2):
    if num1==num2:
        return num1
    elif num1<num2:
        return (num1*num2)/punto_12(num1,(num2-num1))
    else:
        return (num1*num2)/punto_12((num1-num2),num2)

def punto_14(num):
    suma=0
    if num//10==0:
        return num
    else:
        suma+=num%10
        num=num//10
        return suma+punto_14(num)

def punto_15(num,flag=0):
    if flag==1:
        return sqrt(num)
    else:
        return punto_15(num,1)//1
    
def punto_16_serie(n):
    if n==0:
        return 2
    else:
        return 2*(-3)**n+punto_16_serie(n-1)

def punto_16(n):
    for i in range(n):
        print(punto_16_serie(i))

def punto_17(lista,n=1):
    print(lista[-n])
    if n<len(lista):
        punto_17(lista,n+1)

def punto_18(matriz,flag=0):
    if flag==0:
        for i in range(len(matriz)):
            punto_18(matriz[i],1)
    else:
        for i in range(len(matriz)):
            print(matriz[i])

def punto_19(n):
    pass

def punto_20(lista,buscado,n=0):
    if lista[n]==buscado:
        return f"se encontro {buscado} en la lista"
    elif n+1!=len(lista):
        print(n)
        return punto_20(lista,buscado,n+1)
    else:
        return f"no se encontro {buscado} en la lista"
    
def punto_21(lista,buscado):
    medio=len(lista)//2
    print(medio)
    print(lista)
    if lista:
        if lista[medio]==buscado:
            return f"se encontro {buscado} en la lista"
        elif buscado<lista[medio]:
            return punto_21(lista[:medio],buscado)
        elif buscado>lista[medio]:
            return punto_21(lista[medio+1:],buscado)        
    else:
        return f"no se encontro {buscado} en la lista"

def punto_22(mochila,n=0):
    if mochila[n]=="sable de luz":
        return f"se encontro el sable de luz en la mochila"
    elif n+1!=len(mochila):
        return punto_22(mochila,n+1),n
    else:
        return f"no se encontro el sable de luz en la mochila"
    
print(punto_22(["a","b","sable de luz"]))