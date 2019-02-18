#! /usr/bin/env python3


'''
Expand the stopwatch project from this chapter so that it uses
the rjust() and ljust() string methods to “prettify” the output.

Note that you will need string versions of the lapNum, lapTime,
and totalTime integer and float variables in order to call the string methods on them.

Next, use the pyperclip module introduced in Chapter 6 to copy the text output
to the clipboard so the user can quickly paste the output to a text file or email.
'''



import pyperclip,time


input('\nWelcome to Prettified Stopwatch!\n\nPress enter to begin!\n\nPress enter again to "Lap"!\n\nPress "CTRL C" to exit and copy Lap data to clipboard!\n')

print('Started Stopwatch!\n')

start_time= time.time() # epoch time in seconds

last_time= start_time

lap_num= 1

lap_data = '\nLap Data\n\n'

try:
    while True:

        input()

        lap_time = round(time.time() - last_time, 2)

        total_time = round(time.time() - start_time, 2)

        current_lap = 'Lap #' + str(lap_num).rjust(3) + ': ' + str(total_time).rjust(6) + ' (' + str(lap_time).rjust(5) + ')'

        lap_data = lap_data + current_lap + '\n'

        print(current_lap, end='')


        lap_num += 1

        last_time = time.time()  # reset the last lap time

except KeyboardInterrupt:

    pyperclip.copy(lap_data)

    print('\nFinished\n\nResults now copied to clipboard')
