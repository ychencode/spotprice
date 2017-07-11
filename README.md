# spotprice
American spot pricing data from http://www.pjm.com/markets-and-operations/energy/day-ahead/lmpda.aspx Just make original data into json format.
## Data Format
```json
{"date":"20170711","price":[21.23,20.28,19.35,18.62,18.71,19.63,21.12,22.32,24.61,26.72,31.42,35.7,38.91,41.1,44.92,48.8,56.43,52.89,43.65,37.9,36.27,33.91,26.76,24.56]}
```
In Json data. The date field is the real date of the data and it also relate the file name downloaded from http://www.pjm.com/markets-and-operations/energy/day-ahead/lmpda.aspx
The price field is the real power price range from the 1 to 24 hour. The index 0 is 1th hour and the last index is 24th hour.