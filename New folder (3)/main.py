import math

# Addım 2: İstifadəçidən x dəyərini və epislon dəyərini al.
x = float(input('x = '))
ϵ = 0.01

# Addım 4: n'i 1 olaraq qeyd et.
n = 1

# Addım 5: Termi (sin(x) ** n) / n olaraq hesabla və y' mənimsət.
term = math.sin(x) / n
y = term

# Addım 6: Döngü başlad
while abs(term) >= epsilon:
    # Addım 6a: Bir sonraki terimi hesabla
    n += 1
    term = (math.sin(x) ** n) / n

    # Addım 6b: y'e term'i əlavə et
    y += term

# Addım 7: Hesablama tamamlandığında, y'i ekrana yaz
print(f'y = sinx + sinx^2/2 + sinx^3/3 + ... hesablanan dəyər: {y}')




