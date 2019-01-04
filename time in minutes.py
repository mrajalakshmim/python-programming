seconds = int(seconds)
status = 'has been running for' if not finished else 'finished in'

minutes, seconds = divmod(seconds, 60)
hours, minutes = divmod(minutes, 60)

periods = [('hours', hours), ('minutes', minutes), ('seconds', seconds)]
time_string = ', '.join('{} {}'.format(value, name)
                        for name, value in periods
                        if value)

print('The script {} {}'.format(status, time_string))
