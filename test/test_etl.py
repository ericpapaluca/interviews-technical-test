import unittest
import os
from sqlalchemy import create_engine

class test_etl_script(unittest.TestCase):
    # SQLite test database file path
    test_db_path = 'sqlite:///test_database.db'
    test_data_path = 'resources/sales_data.csv'
    engine = None

    @classmethod
    def setUpClass(cls):
        # Set up the test SQLite database
        cls._create_test_database(cls)
        

    @classmethod
    def tearDownClass(cls):
        # Clean up the test database
        cls.engine.dispose()
        cls._delete_test_database(cls)
        

    def _create_test_database(self):
        self.engine = create_engine(f'{test_etl_script.test_db_path}', echo=True)

    def _delete_test_database(self):
        # Delete the test SQLite database
        if os.path.exists(self.test_db_path):
            os.remove(self.test_db_path)
    
    # Write your test code here

if __name__ == '__main__':
    unittest.main()
