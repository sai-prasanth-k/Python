#Now, let's see how to print the above pattern using a python program.

#We can divide the above pattern logic into 3 parts
#Part 1: we have spaces and star('*') in first line
#Part 2: we have spaces, star, hollow spaces, star (middle lines)
#Part 3: we have star set('* ') in the last line


N = 7

for i in range(0, N):

    if i == 0: # part- 1 logic

        print('  '* (N-1) + '*')

    elif i == N - 1: # part- 3 logic

        print('* ' * N)

    else:  # part- 2 logic
        left_spaces = '  ' * (N -i-1)

        hollow_spaces = ('  ' * ( i - 1))

        print(left_spaces + '* ' + hollow_spaces + '*')