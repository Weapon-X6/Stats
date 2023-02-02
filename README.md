# Stats
Program that computes some basic statistics on a collection of small positive integers (all values assumed to be less than 1,000)


## Usage
Import the *DataCapture* class, create an instance and add the numbers to the list, when ready to do the stats, call the 
instance method *build_stats()*, then you're ready to get the insights through the provided methods on the newly build *Stats* class.

```python
from main import DataCapture

capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
  
print(stats.less(4))  # return 2 (only two values 3, 3 are less than 4)
print(stats.greater(4))  # return 2 (6 and 9 are greater than 4)
print(stats.between(3, 6))  # return 4 (3, 3, 4 and 6 are between 3 and 6)
```
