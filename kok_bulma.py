#İkinci Dereceden Bir Bilinmeyenli Denklemin Kökleri

# Denklem: ax^2 + bx + c

# Delta b ** 2 - 4*a*c

# birinci kök: (-b - delta ** 0.5) / (2*a)

# ikinci kök: (-b + delta ** 0.5) / (2*a)

a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:"))

delta = b**2 - 4 * a * c

x1= (-b - delta ** 0.5) / (2*a)
x2= (-b + delta ** 0.5) / (2*a)

print("Birinci Kök: {}\nİkinci Kök: {}\n".format(x1,x2))





