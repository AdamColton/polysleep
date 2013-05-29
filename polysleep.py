import math

MAX_SLEEP = 480
MIN_SLEEP = 120
MIN_SECONDARY = 20
SECONDARY_CYCLES = 5

percent = lambda s: 1.0 - (1.0*s - MIN_SLEEP) / ( MAX_SLEEP - MIN_SLEEP)
secondaryTotal = lambda s: s * (secondaryTotal.m * percent(s) + secondaryTotal.b) # s*(mx+b)
secondaryTotal.b = (1.0 * MIN_SECONDARY) / MAX_SLEEP
secondaryTotal.m = ((1.0 * MIN_SLEEP - MIN_SECONDARY) / MIN_SLEEP) - secondaryTotal.b
cycles = lambda s: math.floor( percent(s)*(SECONDARY_CYCLES-1) ) + 1;
secondary = lambda s: secondaryTotal(s) / cycles(s)
primary = lambda s: s - secondaryTotal(s)
totalWake = lambda s: 1440 - s
wake = lambda s: totalWake(s) / (cycles(s) + 1)

hmFormat = lambda m: str(int(m)/60) + ":" + format( int(m) - 60*(int(m)/60), "02d")

pseudoPrime = lambda s: primary(s) + wake(s) + secondary(s)
gain = lambda s: totalWake(s) - totalWake(MAX_SLEEP)

def breakdown(sleep):
    s = []
    if sleep > MAX_SLEEP:
        s.append("ERROR: sleep exceeds MAX_SLEEP, setting to max")
    if sleep < MIN_SLEEP:
        s.append("ERROR: sleep below MIN_SLEEP, setting to min")
    s.append( "== Breakdown for " + hmFormat(sleep) + " sleep ==" )
    s.append( "Primary Sleep: " + hmFormat(primary(sleep)) )
    s.append( "Wake: " + hmFormat(wake(sleep)) )
    s.append( "Nap: " + str(cycles(sleep)) + " X " + hmFormat(secondary(sleep)) )
    s.append( "Total Wakeful Time: " + hmFormat(totalWake(sleep)) )
    s.append( "Gain: " + hmFormat(gain(sleep)) )
    s.append( "Pseudo-primary: " + hmFormat(pseudoPrime(sleep)) )
    s.append( "" )
    return "\n".join(s)

for i in range(MAX_SLEEP, MIN_SLEEP-1, -20):
    print breakdown(i)