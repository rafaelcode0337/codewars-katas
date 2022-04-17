# Calculating with Functions

## This time we want to write calculations using functions and get the results. Let's have a look at some examples:

```
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
```

## Requirements:

<ul>
    <li>There must be a function for each number from 0 ("zero") to 9 ("nine")</li>
    <li>There must be a function for each of the following mathematical operations: plus, minus, times, divided_by</li> 
    <li>Each calculation consist of exactly one operation and two numbers</li>
    <li>The most outer function represents the left operand, the most inner function represents the right operand</li>
    <li>Division should be integer division. For example, this should return 2, not 2.666666...:</li>
</ul>

```
eight(divided_by(three()))
```
