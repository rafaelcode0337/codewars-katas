# Array.diff
## Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

<p>It should remove all values from list a, which are present in list b keeping their order.</p>

```py
array_diff([1,2],[1]) == [2])
```

<p>If a value is present in b, all of its occurrences must be removed from the other:</p>

```py
array_diff([1,2,2,2,3],[2]) == [1,3])
```
