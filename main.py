import matplotlib.pyplot as plot
# set up your lists
numlist = [8, 6, 5, 3]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
#looks like you can use hex
colorlist = ['#FF13F0', 'green', 'pink', 'yellow' ]
explodelist = [0.1, 0.0, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 42)
plot.axis('equal')
plot.savefig('piechart.png')
