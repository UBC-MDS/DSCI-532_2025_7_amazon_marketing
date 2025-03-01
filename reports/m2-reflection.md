# Reflection

## Implementation

We have attempted the challenging question and implemented all components of the proposal and sketch. We have implemented an additional input (the filter bar on the left side) and hooked it up to the visualizations to react to. This will allow users to have more control over the data and be able to narrow down and focus on their specific target customers. 

We have 6 output components: count of both current and expired users, a table showing expiring users, and 3 graphs. We did not deviated from any best practices during implementation. 

However, we did make some changes on our proposed line graph. Since there is not temporal data available, we couldn’t plot ratings over time. Instead, we have made a user ratings density plot. Also, we moved all 3 charts to the right side column, leaving the user counts and table in the left side column. This makes the dashboard look neater and more logical, it also creates more space for the table to display additional rows. 
 
We also included interactivity in the three graphs. Users can hover over the bars or the lines to view the data values or zoom in and out of the graphs if they want to focus on a specific group or wants a detailed view of the data. This will improve user experience and make the dashboard more user friendly and easier to navigate.


## Limitations

Our current visualization has quite a few limiations.

First, when users unselected all options in a checklist, all table entries disappear. This is not ideal. It would be better if the checkboxes are able to accept multiple selections while still requiring at least one selection.

Second, the age range goes from 0-100, however if there is a minimum age to sign up, we should adjust the minimum of the slider accordingly. For example, there are zero entries of users between 0-10 years old. Also, we the maximum age of users could be over 100 years old which we would need to address. These are both features in development. 

Third, the current and expired user count does not change with the filter selection. This is intentional as it shows the real-time number of subscribers of the platform, but it may be confusing for users. In the future, we may add another card that shows the expiring member count, which will change with the filter selection.

Another limitation is our dataset.  Our the dataset was fictional, so we cannot observe meaningful patterns or insights from the dataset. We chose the columns that we thought might be useful, but they may not be as influential as we thought in real life. Using our dashboard to visualize real data may not provide meaningful insights.

Last but not least, the interactivity of the graphs is still very fundamental, we only included the tooltips and the interactive (zoom in/out) feature. Potential future improvements may include click selections and linking the selections between the two bar charts and the density plot.



