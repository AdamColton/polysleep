# polysleep

## Background
I've long been interested in polyphasic sleep. I once used a week long vacation to try it out and the results were disasterous, but informative. The transition was rough, too rough for me to reach a steady pattern in a week.

Since that time I've been researching and considering the issues. This has led me to focus on two aspects:
1. Transitioning from 8-hour monophasic sleep to higher order polyphasic sleep
2. The trade off between conscious hours and cognitive ability

My theory is that by placing the traditional polyphasic sleep patterns on a continuum, we can sleep any number of minutes between the 8-hour norm and the 2-hour Uber-cycle.

This mapping from any number of minutes to a specific sleep pattern would allow an individual to follow a transition path that best fits their individual needs and tapers off at their personal maxiumum rather than a universal 2-hour limit.

Such a mapping may also allow an exchange between conscious hours and cognitive ability. I believe there would be a limit on the liquidity of this exchange, but it may prove workable. Specifically, an individual could quickly drop down to a pattern of more sleep to increase their congnitive functions for some period of time or (more slowly) reduce their sleep time to gain more hours at lower function.

I have many projects I would like to undertake and they exist along a range of congnitive requirements, and within each project different phases have different requirements. If I could get a system such as the one I have suggested working, I would spend some time in a high sleep, high function mode working on the parts of projects that require high cognitive function. I would then drop to a lower sleep, lower function mode to work on parts of projects that require more time and less cognitive function. For example, I may use a period of more sleep to plan a code project and work through some of it's more difficult parts and plan a wood working project and use any of the more dangerous tools (such as power saws) required for that project. Then, when I move to a lower sleep period, I can use the extra hours to work though the more mundane code and finish the wood working project, staying away from any dangerous powertools.

## The Code
This is more a math problem than an actually program. Sleep is divided into primary sleep and secondary sleep - naps. We make a linear progression from MAX_SLEEP to MIN_SLEEP so that at MIN_SLEEP, the length of primary is the same as the length of MIN_SECONDARY - the shortest allowable length of a nap.

The terms in caps are the givens of the problem. Everything is defined by minutes of sleep in a day, this is represented as s in all the lambdas.

### The lambdas

* percent: linear so that given MAX_SLEEP, it returns 0.0 and given MIN_SLEEP it returns 1.0
* secondaryTotal: linear so that given MAX_SLEEP, it returns MIN_SECONDARY and given MIN_SLEEP it returns MIN_SLEEP - MIN_SECONDARY; in other words at MIN_SLEEP, the length of primary is the same as MIN_SECONDARY. Because this is a simple linear formula taking the form s*(mX+b) and the 'm' and 'b' terms were complicated, I extracted them to secondaryTotal.m and secondaryTotal.b for readability.
* cycles: again linear so that given MAX_SLEEP it returns 1 and given MIN_SLEEP it returns MAX_SECONDARY_CYCLES. This lambda returns an int, not a float.
* secondary: how long the individual secondary sleep cycles will be
* primary: how long the primary sleep cycle will be
* totalWake: total wakeful minutes in a day
* wake: how long each individual wake cycle will be

