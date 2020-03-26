import pymysql


class Database:
    def __init__(self, settings):
        host = settings.get('MYSQL')['host']
        user = settings.get('MYSQL')['user']
        password = settings.get('MYSQL')['password']
        db = settings.get('MYSQL')['db']

        self.con = pymysql.connect(host=host, user=user, password=password,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
        self.cur.execute('CREATE DATABASE IF NOT EXISTS %s' % db)
        self.con = pymysql.connect(host=host, user=user, password=password, db=db,
                                   autocommit=True, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS `listings` ('
                         '`id` int(11) NOT NULL auto_increment, '
                         '`title` VARCHAR(500), '
                         '`price` FLOAT, '
                         '`section` VARCHAR(50), '
                         '`num` VARCHAR(200), '
                         '`row` VARCHAR(50), '
                         '`quantity` int(11), '
                         '`brand` int(11), '
                         '`url` VARCHAR(400), '
                         'PRIMARY KEY (`id`))')

    def get_listings_by_brand(self, brand):
        self.cur.execute(f"SELECT * FROM `listings` WHERE `brand`={brand}")
        result = self.cur.fetchall()
        return result

    def remove_all_listings(self):
        self.cur.execute('TRUNCATE TABLE `listings`')
        return

    def save_data(self,
                  title,
                  price,
                  section,
                  num,
                  row,
                  quantity,
                  brand,
                  url):
        query = """INSERT INTO `listings` (`title`,
                `price`,
                `section`,
                `num`,
                `row`,
                `quantity`,
                `brand`,
                `url`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        self.cur.execute(query, (
            title,
            price,
            section,
            num,
            row,
            quantity,
            brand,
            url
        ))

        return
