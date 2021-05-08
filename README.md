# surfs_up

## Overview of the analysis :

In this project, W. Avy wants to gather some information about temperature trends before opening the surf and ice cream shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.


## Results


-	From the histogram chart, In June, the number of warm days with temperature of greater than “75 degrees” is more in compare of December.
-	The average temperature in June (74.9 degrees) is almost 4 degrees higher than that in December (71.0 degrees) 
-	The minimum temperature of June (64 degrees) show the greatest difference which is 8 degrees warmer than it is in December (56 degrees) and the maximum temperature in June (85 degrees) is 2 degrees warmer than it is in December (83 degrees).


#### Summary Statistics for June
  ![June.png](https://github.com/tjavaheripour/surfs_up/blob/main/Resources/June.png)
  
#### Summary Statistics for December 

  ![December.png](https://github.com/tjavaheripour/surfs_up/blob/main/Resources/December.png)

#### June and December Temperatures

  ![June and December.png](https://github.com/tjavaheripour/surfs_up/blob/main/Resources/June%20and%20December.png)



## Summary
Based on the histograms chart and the summary statistics for June and December temperatures, there is no significant difference between the standard deviation, the average, minimum and maximum temperatures throughout the year. However, we should consider some additional analysis in order to determine if the surf and ice cream shop business is sustainable year-round.

Query the precipitation data by month

   june _prcp = session.query(Measurement.date, Measurement.prcp).\ filter(extract('month',Measurement.date)==6).all()

   dec_prcp = session.query(Measurement.date, Measurement.prcp).\ filter(extract('month',Measurement.date)==12).all()






