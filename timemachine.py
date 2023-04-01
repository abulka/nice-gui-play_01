from nicegui import ui


with ui.splitter().classes('h-screen') as splitter:
    with splitter.before:
        with ui.splitter(horizontal=True, value=10) as splitter2:
            with splitter2.before:
                ui.label('BRANCHES '*150)
            with splitter2.after:
                with ui.splitter(horizontal=True, value=20) as splitter2:
                    with splitter2.before:
                        ui.label('COMMITS '*150)
                    with splitter2.after:
                        with ui.splitter(horizontal=True) as splitter2:
                            with splitter2.before:
                                ui.tree([
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
                                ], label_key='id', on_select=lambda e: ui.notify(e.value))

                            with splitter2.after:
                                ui.label('DIFFS '*150)
    with splitter.after:
        ui.label('FILE CONTENT '*150)

ui.run(dark=True)

