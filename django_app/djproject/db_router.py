class DatabaseRouter:
    """
    A router to control DB operations:
    - User model -> 'default' (Postgres)
    - Product model -> 'mysql_db' (MySQL)
    """

    route_app_labels = {"api"}

    def db_for_read(self, model, **hints):
        if model._meta.model_name == "product":
            return "mysql_db"
        if model._meta.model_name == "user":
            return "default"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.model_name == "product":
            return "mysql_db"
        if model._meta.model_name == "user":
            return "default"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # relations only within same DB
        db_obj1 = "mysql_db" if obj1._meta.model_name == "product" else "default"
        db_obj2 = "mysql_db" if obj2._meta.model_name == "product" else "default"
        if db_obj1 and db_obj2:
            return db_obj1 == db_obj2
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == "product":
            return db == "mysql_db"
        if model_name == "user":
            return db == "default"
        # default to allow migrations on default DB for other models
        return db == "default"
