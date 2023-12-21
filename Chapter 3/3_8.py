# Мандри світом

a1 = "everest"
b2 = "pacific ocean"
c3 = 'amsterdam'
d4 = 'french'
e5 = 'usa'

# перелічив місця в яких хочу побувати

places = [ a1, b2, c3, d4, e5]

# завернув їх у список


print(places)

#перевірив список та побачив що вони НЕ в алфавітному порядку

print(sorted(places))

#викликав функцію сортед не змінюючи список

print(places)

#довів що перелік такий самий

places.reverse()
print(places)

#розвернув перелік

places.reverse()
print(places)

#повернув все яе було

places.sort()
print(places)

#впорядкував за абеткою

places.sort(reverse=True)
print(places)

#порядок зворотній до абетки + вивів зміни на екран.


