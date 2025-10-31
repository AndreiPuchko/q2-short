from q2gui import Q2App, Q2Form, Q2CursorModel, q2_mess
from q2db import Q2Db, Q2DbSchema


class App(Q2App):
    def __init__(self, title=""):
        super().__init__("ToDo App")
        self.add_menu("File|ToDo List", lambda: self.form().run(), toolbar=True)
        self.add_menu("File|Color|Dark Mode", lambda: self.set_color_mode("dark"), icon="moon", toolbar=1)
        self.add_menu("File|Color|Light Mode", lambda: self.set_color_mode("light"), icon="sun", toolbar=1)

        self.add_menu("File|-")
        self.add_menu("File|Quit", self.close, toolbar=True, icon="exit")
        self.add_menu("Help|About", lambda: q2_mess("The shortest DB App ever?"), toolbar=True, icon="info")
        self.create_database()

    def form(self):
        form = Q2Form("ToDo")
        form.add_control("uid", "", datatype="int", noform=1, nogrid=1, pk="*")
        form.add_control("todo", "Todo", datatype="text")
        form.add_control("bdate", "Begin Date", datatype="date")
        form.add_control("edate", "End Date", datatype="date")
        form.add_control("done", "Done", control="check")
        form.set_model(Q2CursorModel(self.db.table(table_name="todo")))
        form.actions.add_action("/crud")
        return form

    def create_database(self):
        self.db = Q2Db("sqlite3", database_name=":memory:")
        db_schema = Q2DbSchema()
        db_schema.add(table="todo", column="uid", datatype="int", pk=True)
        db_schema.add(table="todo", column="todo", datatype="text")
        db_schema.add(table="todo", column="bdate", datatype="date")
        db_schema.add(table="todo", column="edate", datatype="date")
        db_schema.add(table="todo", column="done", datatype="char", datalen=1)
        self.db.set_schema(db_schema)


if __name__ == "__main__":
    App().run()
