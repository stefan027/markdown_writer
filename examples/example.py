import pandas as pd
# from markdown_writer.core import MarkdownWriter
from markdown_writer import MarkdownWriter


if __name__ == "__main__":
    md = MarkdownWriter()
    md.h1("Markdown Writer Example")
    md.text("This is an example of a simple Markdown writer in Python.")
    md.h2("Features")
    features = {
        "Headings": [], "Lists": ["Numbered lists", "Nested lists"],
        "Code blocks": [], "Tables from Pandas DataFrames": [],
        "Hyperlinks": [], "Images": [], "Saving to File": []
    }
    md.nested_list_from_dict(features)
    md.h3("Code Block Example")
    md.code_block("md.code_block('Hello, World!')", "python")

    # We can create Markdown tables from pandas DataFrames
    md.h3("Tables from `Pandas`")
    code = """
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["Cape Town", "Johannesburg", "Durban"]
    })
    md.table_from_pandas(df)
    """
    md.code_block(code, "python", remove_indent=4)
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["Cape Town", "Johannesburg", "Durban"]
    })
    md.table_from_pandas(df)

    # Lists
    md.h3("List Example")
    md.code_block(
        """
        # This is how you create a list:
        sports = ["Rugby", "Football", "Cricket"]
        md.list(sports)
        """, "python", remove_indent=8
    )
    md.list(["Rugby", "Football", "Cricket"])

    # Nested lists
    md.h3("Nested List Example")
    md.h4("Using list levels")
    md.text("A simple way to create nested lists is by specifying the list level.")
    md.code_block(
        """
        # This is how you create a nested list:
        md.list(["Sports"], level=1)
        md.list(["Rugby", "Football", "Cricket"], level=2)
        """, "python", remove_indent=8
    )
    md.list(["Sports"], level=1)
    md.list(["Rugby", "Football", "Cricket"], level=2)

    md.h4("Using a dictionary")
    md.text("You can also create nested lists from a dictionary.")
    md.code_block(
        """
        # This is how you create a nested list from a dictionary:
        produce = {
            "Fruits": {
                "Citrus": ["Orange", "Lemon", "Lime"],
                "Berries": ["Strawberry", "Blueberry", "Raspberry"]
            },
            "Vegetables": {
                "Leafy": ["Spinach", "Lettuce"],
                "Root": ["Carrot", "Beetroot"]
            }
        }
        md.nested_list_from_dict(produce)
        """, "python", remove_indent=8
    )
    produce = {
        "Fruits": {
            "Citrus": ["Orange", "Lemon", "Lime"],
            "Berries": ["Strawberry", "Blueberry", "Raspberry"]
        },
        "Vegetables": {
            "Leafy": ["Spinach", "Lettuce"],
            "Root": ["Carrot", "Beetroot"]
        }
    }
    md.nested_list_from_dict(produce)

    # Numbered lists
    md.h3("Numbered List Example")
    md.code_block("""
        # This is how you create a numbered list:
        sports = ["Rugby", "Football", "Cricket"]
        md.numbered_list(sports)
        """, "python", remove_indent=8
    )
    md.numbered_list(["Rugby", "Football", "Cricket"])

    md.h3("Image Example")
    md.text("Cape Town is a spectacular city.")
    md.code_block("md.image(alt_text='Cape Town', url=url)", "python")
    md.image("Cape Town", "https://www.go2africa.com/wp-content/uploads/2024/11/Banner--1920x630.jpg")

    md.h2("Next steps")
    md.numbered_list(["Install MarkdownWriter", "Create Markdown documents", "Enjoy writing in Markdown"])
    md.save("examples/example.md")
    print("Markdown document 'examples/example.md' has been created.")
