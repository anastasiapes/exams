
c = list(raw_input("Enter your text:"))
y= " "
for i in range (len(c)):
    x= ord(c[i])
    if x >= ord('a') and x <= ord('z'):
            if x > ord('m'):
                x -= 13
            else:
                x += 13
    elif x >= ord('A') and x <= ord('Z'):
            if x > ord('M'):
                x -= 13
            else:
                x += 13
    y += chr(x)
print y
