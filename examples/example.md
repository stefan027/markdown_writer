# Markdown Writer Example

This is an example of a simple Markdown writer in Python.

## Features

- Headings
- Lists
  - Numbered lists
  - Nested lists
- Code blocks
- Tables from Pandas DataFrames
- Hyperlinks
- Images
- Saving to File

### Code Block Example

```python
md.code_block('Hello, World!')
```

### Tables from `Pandas`

```python
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Cape Town", "Johannesburg", "Durban"]
})
md.table_from_pandas(df)
```

| Name    |   Age | City         |
|:--------|------:|:-------------|
| Alice   |    25 | Cape Town    |
| Bob     |    30 | Johannesburg |
| Charlie |    35 | Durban       |

### List Example

```python
# This is how you create a list:
sports = ["Rugby", "Football", "Cricket"]
md.list(sports)
```

- Rugby
- Football
- Cricket

### Nested List Example

#### Using list levels

A simple way to create nested lists is by specifying the list level.

```python
# This is how you create a nested list:
md.list(["Sports"], level=1)
md.list(["Rugby", "Football", "Cricket"], level=2)
```

- Sports

  - Rugby
  - Football
  - Cricket

#### Using a dictionary

You can also create nested lists from a dictionary.

```python
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
```

- Fruits
  - Citrus
    - Orange
    - Lemon
    - Lime
  - Berries
    - Strawberry
    - Blueberry
    - Raspberry
- Vegetables
  - Leafy
    - Spinach
    - Lettuce
  - Root
    - Carrot
    - Beetroot

### Numbered List Example

```python
# This is how you create a numbered list:
sports = ["Rugby", "Football", "Cricket"]
md.numbered_list(sports)
```

1. Rugby
2. Football
3. Cricket

### Image Example

Cape Town is a spectacular city.

```python
md.image(alt_text='Cape Town', url=url)
```

![Cape Town](https://www.go2africa.com/wp-content/uploads/2024/11/Banner--1920x630.jpg)

## Next steps

1. Install MarkdownWriter
2. Create Markdown documents
3. Enjoy writing in Markdown

