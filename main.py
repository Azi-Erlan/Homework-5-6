import flet as ft

from db import main_db


def main(page: ft.Page):
    tasks_collumn = ft.Column()


    def add_to_db(name):
        id = main_db.add_new_task(name)
        print(f"Добавлена новая задача: {name} ID: {id}")
        return id

    def edit_db(id, new_value):
        main_db.edit_task(id, new_value)
        print("Задача успешно обновлена!")

    def delete_from_db(id):
        main_db.delete_task(id)

    def clear_completed(e):
        print("нажали кнопку")
        main_db.delete_all_tasks()
        load_from_db()

    def add_task(task_id, task):

        def edit(e):
            edit_db(task_id, task)
            task_text.read_only = True

        def delete(e):
            delete_from_db(task_id)
            tasks_collumn.controls.remove(task_row)

        def to_edit(e):
            if task_text.read_only:
                task_text.read_only = False
            else:
                task_text.read_only = True

        task_text = ft.TextField(
            value=task, expand=True, read_only=True, on_submit=edit
        )
        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=to_edit)
        submit_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=edit)
        delete_button = ft.IconButton(icon=ft.Icons.DELETE, icon_color=ft.Colors.RED_900, on_click=delete)
        # task_id = add_to_db(user_input.value)
        user_input.value = None
        task_row = ft.Row([task_text, edit_button, submit_button, delete_button,])

        return task_row

    def add_new_task(e):
        if user_input.value:
            task_text_value = user_input.value
            id = add_to_db(task_text_value)
            user_input.value = None
            row = add_task(id, task_text_value)
            tasks_collumn.controls.append(row)

    def load_from_db():
        tasks_collumn.controls.clear()

        results = main_db.get_all_tasks()
        if results:
            for id, task in results:
                result = add_task(id, task)
                tasks_collumn.controls.append(result)

    user_input = ft.TextField(label="Новая задача", expand=True, on_submit=add_new_task)
    enter_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_new_task)
    clear_completed_button = ft.Button(
        content=ft.Text("Очистить всё!"),
        on_click=clear_completed
    )

    main_row = ft.Row([user_input, enter_button])

    page.add(main_row, clear_completed_button, tasks_collumn)
    load_from_db()


if __name__ == "__main__":
    main_db.create_tables()
    ft.run(main, view=ft.AppView.WEB_BROWSER)