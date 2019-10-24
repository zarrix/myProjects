#!/bin/python3

# World Population Statistic

from pygal import * 

pie=Pie()
pie.title='World Population'
pie.add('1999',5.3)
pie.add('2015',7.3)
pie.add('2030',8.5)
pie.add('2050',9.7)
pie.add('2100',11.7)
pie.render()


bar=Bar()
bar.title='World Population'
bar.add('1999',5.3)
bar.add('2015',7.3)
bar.add('2030',8.5)
bar.add('2050',9.7)
bar.add('2100',11.7)
bar.render()


line=Line()
line.title='World Population'
line.x_labels=map(str,[1999,2015,2030,2050,2100])
line.add('World Population',[5.3,7.3,8.5,9.7,11.7])
line.render()

# The End
