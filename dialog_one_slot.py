# dialog uses one slot. Looks like the content of the default slot is specified
# by the contents of the with block.

from nicegui import ui

with ui.dialog() as dialog, ui.card():
    ui.label('Hello world!')
    ui.button('Close', on_click=dialog.close)

ui.button('Open a dialog', on_click=dialog.open)

ui.run()

"""
I need some more clarity on slots. I understand how vue quasar uses slots (default and named) to allow the injection of user components into the quasar component. It seems like the components inside a NiceGUI `with:`  end up inside the default slot?

```python
with ui.dialog() as dialog, ui.card():  #<-- parent
    ui.label('Hello world!')
    ui.button('Close', on_click=dialog.close)
```
e.g. in the above example, the card, label and button end up in the default slot of the dialog. Strictly speaking I think the card ends up in the default slot of the dialog, and the label and button end up in the default slot of the card.

What if a quasar component has multiple additional named slots - how can EasyGUI specify the exact slot for content. E.g. a quasar splitter has a "before" and "after" slot - how would that be expressed in EasyGUI (assuming we had a EasyGUI splitter, which we don't yet).

"""