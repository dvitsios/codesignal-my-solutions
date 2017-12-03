Given a binary tree `t` and an integer `s`, determine whether there is a root to leaf path in `t` such that the sum of vertex values equals `s`.

**Example**

- For

```
t = {
    "value": 4,
    "left": {
        "value": 1,
        "left": {
            "value": -2,
            "left": null,
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        },
        "right": null
    },
    "right": {
        "value": 3,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 2,
            "left": {
                "value": -2,
                "left": null,
                "right": null
            },
            "right": {
                "value": -3,
                "left": null,
                "right": null
            }
        }
    }
}
```

and
`s = 7`,
the output should be `hasPathWithGivenSum(t, s) = true`.

This is what this tree looks like:

```
      4
     / \
    1   3
   /   / \
  -2  1   2
    \    / \
     3  -2 -3
```

Path `4 -> 3 -> 2 -> -2` gives us `7`, the required sum.

- For

```
t = {
    "value": 4,
    "left": {
        "value": 1,
        "left": {
            "value": -2,
            "left": null,
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        },
        "right": null
    },
    "right": {
        "value": 3,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 2,
            "left": {
                "value": -4,
                "left": null,
                "right": null
            },
            "right": {
                "value": -3,
                "left": null,
                "right": null
            }
        }
    }
}
```
and
`s = 7`,
the output should be `hasPathWithGivenSum(t, s) = false`.

This is what this tree looks like:

```
      4
     / \
    1   3
   /   / \
  -2  1   2
    \    / \
     3  -4 -3
```

There is no path from root to leaf with the given sum `7`.