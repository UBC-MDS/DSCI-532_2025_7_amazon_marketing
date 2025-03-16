from dash import Output, Input
import altair as alt
import pandas as pd

def register_chart_callbacks(app):
    @app.callback(
        Output("rating_graph", "spec"),
        Input("expiring-table-placeholder", "derived_virtual_data")
    )
    def update_rating_graph(data):
        data = pd.DataFrame(data)
        rating_graph = alt.Chart(data, width='container', height='container').transform_density(
            'Feedback/Ratings',
            groupby=['Gender'],
            as_=['Feedback/Ratings', 'density']
        ).mark_line(strokeWidth=3).encode(
            x=alt.X('Feedback/Ratings:Q', title="Ratings"),
            y=alt.Y('density:Q', title='Density'),
            color=alt.Color('Gender:N',
                            legend=alt.Legend(symbolStrokeWidth=5), scale=alt.Scale(
                                domain=['Male', 'Female'],
                                range=['dodgerblue', 'crimson'])),
            tooltip=['Gender:N', 'Feedback/Ratings:Q', 'density:Q']
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=14
        ).configure_legend(
            labelFontSize=12,
            titleFontSize=14
        )

        return rating_graph.to_dict(format='vega')

    @app.callback(
        Output("purchase_graph", "spec"),
        Input("expiring-table-placeholder", "derived_virtual_data")
    )
    def update_purchase_graph(data):
        data = pd.DataFrame(data)
        purchase_graph = (alt.Chart(data, width='container', height='container').mark_bar(size=40).encode(
            x=alt.X('Purchase History:N',
                    axis=alt.Axis(labelAngle=0),
                    title="Product Categories"),
            y=alt.Y('count()', title="Count"),
            color=alt.Color('Gender:N',
                            legend=alt.Legend(symbolSize=200),
                            scale=alt.Scale(
                                domain=['Male', 'Female'],
                                range=['dodgerblue', 'crimson'])),
            tooltip=['Gender:N', 'count():Q'],
            order=alt.Order('Gender:N', sort='ascending')
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=14
        ).configure_legend(
            labelFontSize=12,
            titleFontSize=14
        ))
        return purchase_graph.to_dict(format='vega')

    @app.callback(
        Output("engagement_graph", "spec"),
        Input("expiring-table-placeholder", "derived_virtual_data")
    )
    def update_engagement_graph(data):
        data = pd.DataFrame(data)
        engagement_graph = (alt.Chart(data, width='container', height='container').mark_bar(size=15).encode(
            y=alt.Y('Engagement Metrics:N',
                    sort=['High', 'Medium', 'Low'],
                    title=None),
            x=alt.X('count()', title='Count'),
            color=alt.Color('Gender:N',
                            legend=alt.Legend(symbolSize=200),
                            scale=alt.Scale(
                                domain=['Male', 'Female'],
                                range=['dodgerblue', 'crimson'])),
            tooltip=['Gender:N', 'count():Q'],
            order=alt.Order('Gender:N', sort='ascending')
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=14
        ).configure_legend(
            labelFontSize=12,
            titleFontSize=14
        ))
        return engagement_graph.to_dict(format='vega')

    
