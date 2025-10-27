"""A simple Markdown writer in Python."""

class MarkdownWriter:
    def __init__(self, document: str = ""):
        self.document = document

    def text(self, content: str, do_print: bool = False):
        self.document += content + "\n\n"
        if do_print: print(content)

    def h1(self, content: str, do_print: bool = False):
        self.document += f"# {content}\n\n"
        if do_print: print(f"# {content}")

    def h2(self, content: str, do_print: bool = False):
        self.document += f"## {content}\n\n"
        if do_print: print(f"## {content}")

    def h3(self, content: str, do_print: bool = False):
        self.document += f"### {content}\n\n"
        if do_print: print(f"### {content}")

    def h4(self, content: str, do_print: bool = False):
        self.document += f"#### {content}\n\n"
        if do_print: print(f"#### {content}")

    def h5(self, content: str, do_print: bool = False):
        self.document += f"##### {content}\n\n"
        if do_print: print(f"##### {content}")

    def hyperlink(self, text: str, url: str):
        self.document += f"[{text}]({url})\n\n"

    def list(self, items: list, level: int = 1, do_print: bool = False):
        content = ""
        for item in items:
            content += f"{'  ' * (level - 1)}- {str(item)}\n"
        self.document += content + "\n"
        if do_print: print(content)

    def numbered_list(self, items: list, do_print: bool = False):
        content = ""
        for index, item in enumerate(items, start=1):
            content += f"{index}. {str(item)}\n"
        self.document += content + "\n"
        if do_print: print(content)

    def nested_list_from_dict(self, d: dict):
        def _add_items(d: dict, level: int, content=""):
            for key, value in d.items():
                content += f"{'  ' * (level - 1)}- {str(key)}\n"
                if isinstance(value, dict):
                    content = _add_items(value, level + 1, content)
                elif isinstance(value, list):
                    for item in value:
                        content += f"{'  ' * level}- {str(item)}\n"
                else:
                    content += f"{'  ' * level}- {str(value)}\n"
            return content

        content = _add_items(d, 1, content="")
        self.document += content + "\n"

    def code_block(self, code: str, language: str = "", remove_indent: int = 0, do_print: bool = False):
        if remove_indent:
            code = "\n".join(line[remove_indent:] for line in code.split("\n"))
        code = f"```{language}\n{code.strip()}\n```\n\n"
        self.document += code
        if do_print: print(code)

    def image(self, alt_text: str, url: str):
        self.document += f"![{alt_text}]({url})\n\n"

    def bold(self, content: str):
        return f"**{content}**"

    def italic(self, content: str):
        return f"*{content}*"

    def table_from_pandas(self, df, index=False, do_print: bool = False):
        """Converts DataFrame to Markdown table"""
        table = df.to_markdown(index=index) + "\n\n"
        self.document += table
        if do_print: print(table)

    def to_html(self):
        raise NotImplementedError("HTML conversion is not implemented yet.")

    def save(self, filename: str):
        with open(filename, 'w') as file:
            file.write(self.document)
