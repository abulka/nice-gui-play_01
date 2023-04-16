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

with ui.splitter().classes('h-screen') as splitter:
    with splitter.before:
        with ui.splitter(horizontal=True, value=10) as splitter2:
            with splitter2.before:
                ui.label('BRANCHES '*150)
            with splitter2.after:
                with ui.splitter(horizontal=True, value=40) as splitter2:
                    with splitter2.before:

                        # this needs to be replaced with selectable row listview
                        # with ui.table(title='Commits', columns=columns, rows=rows, row_key='id', selection='single', on_select=lambda e: ui.notify(e.selection)).classes('w-full').props('dense') as table:
                        #     with table.add_slot('top-right'):
                        #         with ui.input(placeholder='Search').props('type=search').bind_value(table, 'filter').add_slot('append'):
                        #             ui.icon('search')
                        # end

                        grid = ui.aggrid({
                            'columnDefs': [
                                {'headerName': 'Name', 'field': 'name'},
                                {'headerName': 'Age', 'field': 'age'},
                            ],
                            'rowData': [
                                {'name': 'Alice', 'age': 18},
                                {'name': 'Bob', 'age': 21},
                                {'name': 'Carol', 'age': 42},
                            ],
                            'rowSelection': 'multiple',
                        }).classes('max-h-40')

                    with splitter2.after:
                        with ui.splitter(horizontal=True) as splitter3:
                            with splitter3.before:
                                ui.tree(tree_data, label_key='id',
                                        on_select=lambda e: ui.notify(e.value))

                            with splitter3.after:
                                ui.label('DIFFS '*250)
    with splitter.after:
        ui.html(build_html())

ui.run(dark=True)
