# Reflection

## Implementation

We have implemented several additional features in our dashboard to improve its usability and organization. One major enhancement is the addition of a chained callback for the table, allowing the charts to dynamically react to the table filters. We also improved the dashboard’s layout by displaying charts inside a Card component, making the interface cleaner and more organized. To enhance filtering options, we introduced a "Both" option for the Renewal Type and Gender filters and changed the Date Range filter to "Months Till Expire" for better clarity. Additionally, we renamed "Expired Users" to "Expiring Users" so that it dynamically updates based on the filters. A CSV download button has also been added, enabling users to download the currently filtered table data for external analysis.

## Challenges and Limitations

One known corner case in our implementation is that when the table filter returns only a single row, the ratings chart does not display any lines. Despite this, we have used the best practices for effective visualizations and did not intentionally deviate from them. We took inspiration from other groups to improve our design, incorporating a CSV export button after seeing its usefulness in Group 3’s dashboard. Additionally, we modified the age range slider based on Group 12’s design, reducing the number of marks, displaying the current range, and allowing users to select any age value rather than being restricted to fixed ranges. Our dashboard is well-structured, with clear sections dedicated to user data, engagement, and purchasing behavior. The filters in the left panel allow users to filter data effectively, and the "Download CSV" button enhances usability by incorperating download analysis. However, there are some limitations. One notable missing feature is the ability to track how long users stay subscribed before expiring or renewing, which could provide valuable insights into user retention.

## Future Improvements

To further improve the dashboard, we plan to add a map visualization that displays the locations of the most engaged and expired users. Another potential enhancement is highlighting user retention rates over different time periods, allowing for deeper insights into user behavior. These additions would provide a more comprehensive view of the data and improve decision-making capabilities.
