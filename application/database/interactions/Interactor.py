from application.database.client.client import MySqlConnection
from application.database.exceptions import UserNotFoundException
from application.database.models.models import Base, User


class DBInteraction:
    def __init__(self, host, port, user, password, db_name, rebuild_db=False):
        self.mysql_connection = MySqlConnection(host=host, user=user,
                                                port=port, password=password, db_name=db_name,
                                                rebuild_db=rebuild_db)

        self.engine = self.mysql_connection.connection.engine

        if rebuild_db:  # порядок важен (из-за внешнего ключа в муз композициях, направленного на юзерс)
            self.create_table_users()
            self.create_table_musical_compositions()

    def create_table_users(self):
        if not self.engine.dialect.has_table(self.engine, 'users'):
            Base.metadata.tables['users'].create(self.engine)
        else:
            self.mysql_connection.execute_query(f'DROPTABLE IF EXISTS users')
            Base.metadata.tables['users'].create(self.engine)

    def create_table_musical_compositions(self):
        if not self.engine.dialect.has_table(self.engine, 'musical_compositions'):
            Base.metadata.tables['musical_compositions'].create(self.engine)
        else:
            self.mysql_connection.execute_query(f'DROPTABLE IF EXISTS musical_compositions')
            Base.metadata.tables['musical_compositions'].create(self.engine)

    def add_user_info(self, username, email, password):
        user = User(
            username=username,
            password=password,
            email=email
        )
        self.mysql_connection.session.add(user)
        return True

    def get_user_info(self, username):
        user = self.mysql_connection.session.query(User).filter_by(username=username).first()
        if user:
            self.mysql_connection.session.expire_all()
            return {'username': user.username, 'email': user.email, 'password': user.password}
        else:
            raise UserNotFoundException('User not found')


if __name__ == '__main__':
    db = DBInteraction(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='pass',
        db_name='test',
        rebuild_db='True'
    )
    pass
