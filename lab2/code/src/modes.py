'''
    This file contains some constants to help manage the app's two
    display modes, Percent and Count.
'''

MODES = dict(Count='Count', Percent='Percent')
MODE_TO_COLUMN = {MODES['Count']: 'PlayerLine', MODES['Percent']: 'PlayerPercent'}
