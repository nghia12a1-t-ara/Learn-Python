messages = '''With the above code, we are defining a “dummy” section inside the final binary file. Using the
location counter operator (“.”) we increment the size of this section so that it has a dimension equal
to the maximum heap size and the “estimated” minimum stack size. If the sum of .data, .bss, stack
and heap regions is greater than the SRAM size, the linker will emit an error, as shown below:
'''

count = {}

for character in messages:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
