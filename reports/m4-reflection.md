# Milestone 4 Reflection

## Implementation

Throughout the development of our dashboard we found the DSCI 532 lecture notes were good for creating and structuring the dashboards, as well as the DSCI 531 lecture notes helped us with the visualizations. The Dash documentation helped as well when trying to find resouces not found in the course textbook. Other resources such as Dash tutorials, examples, and repositories such as Dash Example Index and the Awesome Dash Repo were helpful for troubleshooting.

Since Milestone 3, we have refined the app more and added a few features. We cached the radio button filters to improve performance and fixed a bug in the download CSV button to make it work properly. We addressed minor spelling errors, and added the Amazon logo as a favicon and updating the tab title to the dashboard name. Additionally, we optimized data processing by reading from a Feather file instead of a CSV, which improved the loading speed. Another improvement was updating the app layout and style so the font size and widget height will change dynamically, this will make it easier to use across different devices. For the challenging exercise of this milestone, we added proper docstrings to functions in the src/callback folder.

While implementing the dashboard we changed some design choices from our original proposal which was recommended from peer reviews. We renamed the table title to “Upcoming Renewals Needed” to avoid negative connotations associated with expiring memberships. As well as, we also moved the “Membership End Date” column to the first position to emphasize the most critical information people need to review.

A corner case we encountered is that when the table filter results in only one row of data, the ratings chart does not display any lines. This issue is because the density plot used in the visualization requires more than a single x-value to generate a distribution.

Currently, our dashboard is structured well, with clear sections displaying user data, engagement metrics, and purchasing behavior. The filters on the left panel effectively filter the displayed data, and the "Download CSV" button allows users to analyze the information externally. Additionally, caching radio button selections has noticeably improved performance. The adaptive font and chart sizing ensure a consistent user experience across different screen sizes.

## Challenges and Limitations

Some limitations in our dashboard are that it would be better to include insights on user retention duration, such as, how long users stay subscribed before expiring or renewing. Additionally, while the DataTable supports filtering, it does not currently allow users to select specific rows or cells for further analysis.

## Future Improvements

Potential future improvements that could enhance the dashboard are a map visualization could help provide insights into the geographic distribution of engaged versus expired users. We could also incorporate user retention trends over different time periods to help identify renewal patterns. As well as adding the ability to select specific table cells would enhance interactivity, allowing users to refine their analysis manually.
