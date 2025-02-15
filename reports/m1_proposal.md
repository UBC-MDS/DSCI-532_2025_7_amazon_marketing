# Amazon Prime Customer Dashboard Proposal

By Julian Daduica, Mavis Wong, and Yixuan Gao

# Motivation and Purpose

Our role: Data Science Consultancy Firm

Target Audience: Amazon Prime’s Customer Engagement and Marketing Teams

We are creating this dashboard to empower Amazon Prime’s Customer Engagement and Marketing Teams with data-driven insights to improve user retention. As a Data Science Consultancy Firm, our role is to analyze user demographics, engagement patterns, and content preferences to uncover trends that influence subscription renewals.

The key challenge Amazon Prime faces is understanding why certain users choose not to renew their subscriptions and identifying strategies to enhance retention. This is crucial because retaining existing customers is more cost-effective than acquiring new ones, and higher engagement leads to increased revenue and brand loyalty.

Our dashboard will provide interactive visualizations and filters that allow stakeholders to explore renewal behavior, engagement levels, and purchase history. By identifying patterns—such as the impact of engagement, subscription type, and product preferences on renewals—marketing teams can implement targeted campaigns, personalized offers, and strategic content recommendations to boost retention rates.


# Description of the data

The dataset we will be using is the Amazon Prime Users Dataset from
[Kaggle](https://www.kaggle.com/datasets/arnavsmayan/amazon-prime-userbase-dataset).
This dataset contains information on 2,550 fictional users of the Amazon
Prime subscription service and has 19 columns related to user
demographics, subscription details, engagement, and preferences.

From this dataset, we plan to derive two new variables, `Age` and
`Months Till Expire`, to help us analyze engagement patterns and user
preferences across different age groups, as well as identify users
nearing the end of their subscriptions so that appropriate follow-up
actions, such as targeted marketing strategies, can be implemented to
retain customers.

Due to time constraints, our visualization and analysis will focus on
the following nine variables:

User Demographics:

-   `Gender` : User's gender (Male/Female)

-   `Age` : User's age, derived from `Date of Birth`.

Subscription Details:

-   `Subscription Plan` : The type of subscription (Annual
    Subscription/Monthly Subscription).

-   `Renewal Status` : Whether auto-renewal or manual renewal is set up
    for the subscription.

-   `Months Till Expire` : The number of months left until a user's
    subscription expires, derived from `Membership End Date`.

User Engagement Patterns:

-   `Feedback/Ratings` : The average rating the user gives to services
    or products.

-   `Engagement Metrics` : The degree of user engagement on the platform
    (High/Medium/Low).

Content/Product Preferences:

-   `Favorite Genres` : User preferences for books, movies, and other
    contents (e.g., Horror, Sci-Fi).

-   `Purchase History` : User's recent purchase type (e.g., Electronics,
    Clothing).

While we will not use users' personal information (such as email or
username) for analytical purposes, our dashboard will include a table
displaying the contact information (email, name, etc.) of customers
nearing the end of their subscriptions for targeted follow-up.

# Research questions

Bob is a Senior Customer Engagement Manager at Amazon Prime, and he
wants to understand how user demographics, engagement patterns, and
content preferences affect subscription renewals so that he can develop
targeted strategies to improve user retention. He wants to be able to
explore customer data to compare renewal rates across different user
filters and identify trends that influence renewal behaviors.

When Bob logs on to the Amazon Prime Customer Retention Dashboard, he
will see insights of user data, including trends in renewal behavior,
purchase history, and engagement levels. He can filter the data by key
variables like subscription type (manual vs. auto-renewal) or
demographics (age, gender). This allows him to explore insights such as
whether higher engagement correlates with increased renewal rates or if
certain product categories drive higher retention.

For example, Bob might notice that users who manually renew their
subscriptions tend to have lower engagement compared to auto-renew
users. By exploring the Purchase History section, he discovers that
users who purchase electronics have higher renewal rates, whereas book
and clothing buyers show more frequent non-renewals. In the Rating Over
Time section, he identifies a decline in user satisfaction among those
whose subscriptions are about to expire, which could signal
dissatisfaction and a potential reason for not renewing the
subscription.

Based on these insights, Bob can now develop actionable strategies. Now,
Bob can propose to higher executives or marketing teams to offer
incentives for users to switch to auto-renewal to increase retention. He
could also suggest prioritizing electronics-related content in marketing
campaigns since it shows a positive correlation with renewals. To
address the decline in user satisfaction, Bob could recommend improving
customer support or improving content to these customers.

# App sketch and description

![Amazon Prime Customer Retention Dashboard Sketch](../img/sketch.png)

Description: