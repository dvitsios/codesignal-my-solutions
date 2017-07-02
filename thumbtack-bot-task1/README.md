In Thumbtack, users are able to rate Pros based on their experience working with them. Each rating is an integer ranging from `1` to `5`, and all ratings are averaged to produce a single number rating for any given Pro. Those Pros who have a rating lower than a specified `threshold` are manually reviewed by Thumbtack staff to ensure high quality of service.

You're given a list of `ratings` for some Pros. Find out which Pros should be manually reviewed.

Example

For `threshold = 3.5` and

```

ratings = [[3, 4],
           [3, 3, 3, 4],
           [4]]

```

the output should be `ratingThreshold(threshold, ratings) = [1]`.

Assume that we have `3` Pros that have received the following ratings: `[3, 4], [3, 3, 3, 4]` and `[4]`. Then
And if `threshold = 3.5` the answer is `ratingThreshold(threshold, ratings) = [1]`.
The first Pro's rating is `3.5`, the second one's is `3.25`, and the last one's is `4`, so only the second Pro should be reviewed manually (the output is their 0-based index).
