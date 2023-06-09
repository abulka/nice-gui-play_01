import time
from nicegui import ui
from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates/")) # jinja templating
lang = 'python'

def setup_prism():
    template_head = environment.get_template("head.html")
    ui.add_head_html(template_head.render(lang=lang))

setup_prism()

def build_html():
    source_file_contents = open('timemachine.py').read()
    js_file_contents = ''
    template = environment.get_template("template2.html")
    html_str = template.render(lang=lang, source_file_contents=source_file_contents, js_file_contents=js_file_contents)
    return html_str

# ui.aggrid

commits_columns = [
        {'headerName': 'SHA', 'field': 'sha', 'resizable': True },
        {'headerName': 'Comment', 'field': 'comment', 'resizable': True },
        {'headerName': 'Date', 'field': 'date', 'resizable': True },
        {'headerName': 'Author', 'field': 'author', 'resizable': True },
    ]

commits_rows = [
        {'sha': 'a789238479237hhhk', 'date': '2020-01-01', 'author': 'Alice', 'comment': 'Initial commit'},
        {'sha': 'b789238479237hhhk', 'date': '2020-01-02', 'author': 'Bob', 'comment': 'Added a feature'},
        {'sha': 'c7892oiu99977yyee', 'date': '2020-01-03', 'author': 'Carol', 'comment': 'Fixed a bug'},
        {'sha': 'd7892oiu99977yyee', 'date': '2020-01-04', 'author': 'Dave', 'comment': 'Added a feature'},
        {'sha': 'e7892oiu99977yyee', 'date': '2020-01-05', 'author': 'Eve', 'comment': 'Fixed a bug'},
        {'sha': 'f7892oiu99977yyee', 'date': '2020-01-06', 'author': 'Frank', 'comment': 'Added a feature'},
        {'sha': 'g7892oiu99977yyee', 'date': '2020-01-07', 'author': 'Grace', 'comment': 'Fixed a bug'},
        {'sha': 'h7892oiu99977yyee', 'date': '2020-01-08', 'author': 'Helen', 'comment': 'Added a feature'},
        {'sha': 'i789238479237hhhk', 'date': '2020-01-09', 'author': 'Ivan', 'comment': 'Fixed a bug'},
        {'sha': 'j789238479237hhhk', 'date': '2020-01-10', 'author': 'John', 'comment': 'Added a feature'},
        {'sha': 'k78v1v12v12312nhk', 'date': '2020-01-11', 'author': 'Karl', 'comment': 'Fixed a bug'},
        {'sha': 'l78v1v12v12312nhk', 'date': '2020-01-12', 'author': 'Linda', 'comment': 'Added a feature'},
        {'sha': 'm78v1v12v12312nhk', 'date': '2020-01-13', 'author': 'Mike', 'comment': 'Fixed a bug'},
        {'sha': 'n78v1v12sdfjlkjcc', 'date': '2020-01-14', 'author': 'Nancy', 'comment': 'Added a feature'},
        {'sha': 'o78v1v12sdfjlkjcc', 'date': '2020-01-15', 'author': 'Oscar', 'comment': 'Fixed a bug'},
        {'sha': 'p78v1v12sdfaabbccj', 'date': '2020-01-16', 'author': 'Pam', 'comment': 'Added a feature'},
        {'sha': 'q7892384sdfaabbccj', 'date': '2020-01-17', 'author': 'Quentin', 'comment': 'Fixed a bug'},
        {'sha': 'r7892384sdfaabbccj', 'date': '2020-01-18', 'author': 'Ruth', 'comment': 'Added a feature'},
        {'sha': 's7892384sdfaabbccj', 'date': '2020-01-19', 'author': 'Steve', 'comment': 'Fixed a bug'},
        {'sha': 't7892384792aabbhhk', 'date': '2020-01-20', 'author': 'Tina', 'comment': 'Added a feature'},
        {'sha': 'u7892384792aabbhhk', 'date': '2020-01-21', 'author': 'Ursula', 'comment': 'Fixed a bug'},
    ]

# ui.table

columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True},
    {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
]
rows = [
    {'id': 0, 'name': 'Alice', 'age': 18},
    {'id': 1, 'name': 'Bob', 'age': 21},
    {'id': 2, 'name': 'Lionel', 'age': 19},
    {'id': 3, 'name': 'Michael', 'age': 32},
    {'id': 4, 'name': 'Julie', 'age': 12},
    {'id': 5, 'name': 'Livia', 'age': 25},
    {'id': 6, 'name': 'Carol'},
]

# ui.tree

tree_data = [
    {'id': 'numbers', 'children': [
        {'id': '1', 'children': [
            {'id': '11'},
            {'id': '12', 'children': [
                {'id': '121'},
                {'id': '122'}
            ]}
        ]},
        {'id': '2', 'children': [
            {'id': '21'},
            {'id': '22'}
        ]}
    ]},
    {'id': 'letters', 'children': [
        {'id': 'A', 'children': [
            {'id': 'AA'},
            {'id': 'AB'}
        ]},
        {'id': 'B', 'children': [
            {'id': 'BA'},
            {'id': 'BB'}
        ]}
    ]}
]

class FileTree:
    def __init__(self) -> None:
        self.data = tree_data
        self.selected = None
        # self.expanded = ['numbers', 'letters']
        self.expanded = ['A']
tree = FileTree()

#  branches

class Branches:
    def __init__(self) -> None:
        self.options = ['master', 'main', 'experiment', 'branch2', 'branch2a']
        self.current_branch = self.options[0]

branches = Branches()

with ui.splitter(value=40).classes('h-screen') as splitter:
    with splitter.before:
        with ui.row().style('align-items: center;'):
            ui.label('Branch:')
            select2 = ui.select(branches.options).bind_value(branches, 'current_branch')
        with ui.splitter(horizontal=True, value=40) as splitter2:
            with splitter2.before:

                grid = ui.aggrid({
                    'columnDefs': commits_columns,
                    'rowData': commits_rows,
                    'rowSelection': 'single',
                }).on('rowSelected', lambda msg: print(msg)).classes(add='p-1 h-full ag-theme-alpine-dark', remove='ag-theme-balham')

            with splitter2.after:
                with ui.splitter(horizontal=True) as splitter3:
                    with splitter3.before:
                        mytree = ui.tree(tree_data, label_key='id',
                                on_select=lambda e: ui.notify(e.value)).props('dense selected-color="blue"')
                                # on_select=lambda e: ui.notify(e.value)).props('default-expand-all dense selected-color="red"')
                                # on_select=lambda e: ui.notify(e.value)).props('expanded=["letters"]')
                                # on_select=lambda e: ui.notify(e.value)).props(f'expanded={tree.expanded}')
                        ui.button('Expand all').on('click', lambda e: mytree.run_method('expandAll'))
                        ui.button('Collapse all').on('click', lambda e: mytree.run_method('collapseAll'))
                        ui.button('Get Selected').on('click', lambda e: ui.notify(mytree._props.get('selected')))
                        ui.button('Get Expanded').on('click', lambda e: ui.notify(mytree._props.get('expanded')))
                        ui.button('getExpandedNodes').on('click', lambda e: ui.notify(mytree.run_method('getExpandedNodes')))
                        # ui.button('Set Expanded').on('click', lambda e: mytree.props(add='expanded=["letters"]'))
                        # ui.button('Set Expanded').on('click', lambda e: mytree.props('expanded=["letters"]'))
                    with splitter3.after:
                        ui.label('DIFFS '*250)
    with splitter.after:
        ui.html(build_html())

ui.run(dark=True)
