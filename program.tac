a = 2
b = 3
t1 = "Здравей "
c = t1
t2 = "свят!"
d = t2
e = False
t3 = a + b
print t3
t4 = c + d
print t4
t5 = a + b
t6 = t5 + 1
t7 = t6 / 3
t8 = t7 * 10
print t8
t9 = 3 > 1
if t9 goto L1
goto L3
L1:
p = 11
print p
goto L2
L3:
t10 = "Все работает!"
t11 = " здр"
t12 = t10 + t11
print t12
L2:
if e goto L4
goto L6
L4:
t13 = "итмо"
print t13
goto L5
L6:
L7:
t14 = b > 0
if t14 goto L8
goto L9
L8:
t15 = "МНОГО"
print t15
t16 = b - 1
b = t16
goto L7
L9:
L5:
