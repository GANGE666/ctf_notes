

s = ''',[->>+++++++>>+++++>>+++>>++>>++++>++++++<<+++<<+++++++++<<++++++++<<
++++++<<++++++++<]>[->>+++++>>+++++++++>>+++++++++>>++>>++++<+++++++++<<++++<<++++<<++<<++<]<,[->>++
+++>>++++++++>>++++++>>+++++++>>+++++++>++++++<<++++++<<++++++++<<+++<<+++<<++++++++<]>[->>++++++++>
>+++>>+++++++>>++++>>+++++++++<++++++<<+++++++++<<++<<+++++++++<<++++++++<]<,[->>++++++++>>+++++++>>
++>>++>>+++++++++>+++<<++++<<+++<<+++++<<++++++++<<++++++++<]>[->>++++>>++++++++>>++++++>>++++++>>++
+++<++++<<+++++++++<<++++++++<<+++++++<<++++<]<,[->>+++++>>+++++++++>>+++>>++++>>++++>+++<<++++++++<
<++++++<<+++++<<++++++<<++++++++<]>[->>++++++>>++++++>>+++++>>++++++++>>+++++++<++++++++<<++++++<<++
+++<<+++<<+++++++<]<,[->>+++++++>>++++>>++++>>+++>>+++++++>+++++++<<+++++++++<<+++++<<+++++<<+++++++
<<++++++++<]>[->>+++>>++++>>++++>>+++++>>++++++<++++<<+++<<++++++++<<+++++++<<+++++<]<,[->>+++++>>++
>>++++>>+++>>++++++>++<<+++++++<<++++<<+++++++++<<+++++++<<++++++++<]>[->>++>>+++++++++>>+++++>>++++
++++>>+++++++++<+++++++<<++<<++++<<+++<<++<]<,[->>++++++>>+++++++>>+++>>++++++>>++++++++>++<<++++<<+
++<<++++++++<<++++++<<++++++++<]>[->>++++++>>++>>+++++++++>>++++>>++++++<+++++<<++++<<++++++++<<++++
<<+++++++<]<,[->>+++++++++>>++++++++>>++++++>>+++++++>>+++++++++>++<<++++++++<<+++++<<+++++<<+++<<++
++++++<]>[->>+++++++++>>+++++++>>+++++++++>>++++>>++<+++++++<<+++++++++<<++<<+++<<++++++++<]<,[->>++
>>++++++++>>++>>++++++>>+++++>++++<<++++<<+++++++<<+++++++<<++++++++<<++++++++<]>[->>+++++++>>++>>++
++++++>>+++++++>>++++<++<<+++<<+++++++<<+++++<<++<]<,[->>+++++++++>>+++++++>>+++++>>++++>>++>+++++<<
+++++<<++<<++<<+++++<<++++++++<]>[->>++++++++>>++++++>>++>>+++++>>+++++++++<++++++++<<++++++++<<++++
<<++++<<+++++++++<]>++.>++++++.>++++++++.>++++++++.>+++.>+++++.>+++++.>+++++++.>++++.>+++++++++.'''

f = open("10_11_2.py", "w")

f.write('''array = [0] * 10000
index = 0
''')

array = [0] * 10000
index = 0

count = 0

loop = 0

for c in s:
    if c == '\n':
        continue

    if c == '+':
        count += 1
        continue
    else:
        if count != 0:
            if loop == 1:
                f.write("\t")
            f.write("array[%s] = (array[%s] + %s) %% 256\n" % (index, index, count))
            count = 0

        if c == ',':
            if loop == 1:
                f.write("\t")
            f.write("array[%s] = int(input())\n" % index)
        elif c == '>':
            # f.write("index += 1\n")
            index += 1
        elif c == '<':
            # f.write("index -= 1\n")
            index -= 1
        elif c == '-':
            if loop == 1:
                f.write("\t")
            f.write("array[%s] -= 1\n" % index)
        elif c == '.':
            if loop == 1:
                f.write("\t")
            f.write("print(array[%s])\n" % index)
        elif c == '[':
            f.write("while array[%s]:\n" % index)
            loop = 1
        elif c == ']':
            f.write("\n")
            loop = 0

