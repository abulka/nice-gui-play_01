# See https://github.com/zauberzeug/nicegui/discussions/774#discussioncomment-5704157

from nicegui import ui

ui.add_head_html('''
<style>
.selected {
  color: white;
  background: #59aef2; /* blue */
}
</style>
''')

multiple_selection = False
                 
def toggle_select(row: dict) -> None:
    if multiple_selection:
        if row in table.selected:
            table.selected.remove(row)
        else:
            table.selected.append(row)
    else:
        table.selected.clear()
        table.selected.append(row)
    print('toggle_select', row, table.selected)
    table.update()

columns = [{'name': 'name', 'label': 'Name', 'field': 'name'},
              {'name': 'age', 'label': 'Age', 'field': 'age'}
           ]
rows = [{'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 30}, {'name': 'Carol', 'age': 40}]
with ui.table(columns=columns, rows=rows, row_key='name') as table:
    ui.label('hi there')
    table.add_slot('body-cell', r"""
        <q-td :props="props" @click="$parent.$emit('cell_click', props)">
            {{ props.value }}
        </q-td>
    """)
    table.on('cell_click', lambda msg: toggle_select(msg['args']['row']))

# Display the selected row, luckily bind_text_from() works
ui.label().bind_text_from(table, 'selected', lambda val: f'Current selection: {val[0]["name"] if val else "None"}')

ui.run()
