On Quora, a question can have a variety of user-submitted answers. These questions are assigned topic tags to improve discoverability, and views are tracked at the answer level to identify the top answers and surface them in the the feed and search results.

More specifically:

 * A user can write an answer to a question;
 * A question can have multiple answers;
 * A question can be assigned multiple topics;
    * For example, the question "How many software engineers work at Google as of 2017?" is tagged with the topics "Silicon Valley", "Google", and "Software Engineering".
 * An answer can get views.

The Most-Viewed Writers for a given topic are the top 10 Quora users whose answers to questions tagged with that topic are viewed the most. (When fewer than 10 users have submitted answers to questions tagged with a particular topic, the Most-Viewed Writers for that topic would include all the users who have contributed answers, regardless of whether or not their answers have any views.) An answer must belong to a question that is tagged with a given topic to be considered to be within that topic.

Given this system, compute the Most Viewed Writers for each topic, ordered from the smallest `topic_id` to the largest one. If two users have the same number of views, the user with the smaller user_id should come first.

For a specific `topic_id`, the set of Most-Viewed Writers should be returned in the following format:

 * <user_id_1> <views_1>
 * <user_id_2> <views_2>
 * ...
 * <user_id_N> <views_N>

where:

 * `user_id_i` is the ID of the `ith` user in the set;
 * `views_i` is the total number of views the user gets across all their answers in that topic;
	 * Note that `views_i` may be equal to `0`. If a user posted an answer that didn't get any views, they can still be included in the Most Viewed Writers list if there are fewer than `10` users who have contributed answers for that topic;
 * `N` is the number of Most Viewed Writers for the topic `topic_id`.

**Example**

For `topicIds = [[1, 2, 3], [2, 3, 4], [1, 4], [2, 3]]`,

`answerIds = [[6, 4], [1, 2], [5], [3]]` and

`views = [[2, 1, 2], [6, 3, 5], [3, 3, 0], [5, 1, 1], [4, 2, 3], [1, 4, 2]]`, the output should be:

```

mostViewedWriters(topicIds, answerIds, views) = [
    [[3, 5], [2, 3], [1, 1]],
    [[3, 5], [2, 3], [1, 2], [4, 2]],
    [[3, 5], [2, 3], [1, 2], [4, 2]],
    [[1, 3], [4, 2]]
]

```

In this example, we have `4` different topic IDs: `1`, `2`, `3`, and `4`. Let's find the Most Viewed Writers for each of them.

 * **For `topic_id = 1`**:
	 * As we can see in the `topicIds` array, topic `1` is tagged to questions `0` and `2`.
	 * We can see in the `answerIds` array that the answers corresponding to this topic are `6`, `4`, and `5`.
 	 * Now let's look at the `views` array and find all such `views[i]` that `views[i][0]` is one of the answer IDs from the last line:
		`views[1][0] = 6`, so we add `views[1][2] = 5` views to the user with ID `views[1][1] = 3`;
		`views[3][0] = 5`, so we add `views[3][2] = 1` views to the user with ID `views[3][1] = 1`;
		`views[4][0] = 4`, so we add `views[4][2] = 3` views to the user with ID `views[4][1] = 2`.
 * To recap, for `topic_id = 1` we have `3` Most Viewed Writers: the user with ID `3` has `5` views, the user with ID `2` has `3` views, and the user with ID `1` has `1` view.

 * **For `topic_id = 2`**:
 	* As we can see in the topicIds array, topic `2` is tagged to questions `0`, `1`, and `3`.
	* We can see in the answerIds array that the answers corresponding to this topic are `6`, `4`, `1`, `2`, and `3`.
 	* Now let's look at the `views` array and find all such `views[i]` that `views[i][0]` is one of our answer IDs:
		`views[1][0] = 6`, so we add `views[1][2] = 5` views to the user with ID `views[1][1] = 3`;
		`views[4][0] = 4`, so we add `views[4][2] = 3` views to the user with ID `views[4][1] = 2`;
		`views[5][0] = 1`, so we add `views[5][2] = 2` views to the user with ID `views[5][1] = 4`;
		`views[0][0] = 2`, so we add `views[0][2] = 2` views to the user with ID `views[4][1] = 1`;
		`views[2][0] = 3`, so we add `views[3][2] = 0` views to the user with ID `views[3][1] = 3`.

 * To recap, for `topic_id = 2` we have `4` Most Viewed Writers: the user with ID `3` has `5` views, the user with ID `2` has `3` views, the user with ID `1` has `2` views, and the user with ID `4` has `2` views. The last two users are ordered as they are because the user with the smaller ID comes first.

 * **For `topic_id = 3`**:
 	* This topic is tagged to the same questions as `topic_id = 2` is, so its Most Viewed Writers is also the same.

 * **For `topic_id = 4`**:
 	* As we can see in the `topicId` array, this topic is tagged to questions `1` and `2`.
 	* We can see in the `answerId` array that the answers corresponding to this topic are `1`, `2`, and `5`.
 	* Now let's look at the `views` array and find all such `views[i]` that `views[i][0]` is one of our above answer IDs:
		`views[5][0] = 1`, so we add `views[5][2] = 2` views to the user with ID `views[5][1] = 4`;
		`views[0][0] = 2`, so we add `views[0][2] = 2` views to the user with ID `views[0][1] = 1`;
		`views[3][0] = 5`, so we add `views[3][2] = 1` views to the user with ID `views[3][1] = 1`.
 * To recap, for `topic_id = 4` we have `2` Most Viewed Writers: the user with ID `1` has `3` views, and the user with ID `4` has `2` views.
