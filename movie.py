movie = input("Movie: ")
t = int(input("Tickets: "))
print("Total =", t * 150)

movies = {"1": ("Avatar", 200), "2": ("Batman", 150)}
choice = input("1.Avatar 2.Batman: ")
t = int(input("Tickets: "))
print("Total =", movies[choice][1] * t)

m = {"A":150, "B":200}
c = input("Movie A/B: ")
t = int(input("Tickets: "))
print("Pay =", m[c] * t)