# Function to set up display options for pandas
def setup_pandas_display():
    # Increase display limits
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)

# Function to make DataFrame scrollable in the notebook output
def make_scrollable(df):
    style = (
        '<style>'
        'div.output_scroll {'
        'resize: both;'
        'overflow: auto;'
        '}'
        '</style>'
    )
    html = f"{style}{df.to_html()}"
    display(HTML(html))

# Main function to display DataFrame
def display_dataframe(df):
    setup_pandas_display()    # Enable scrollable view
    make_scrollable(df)
