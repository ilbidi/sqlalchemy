# Test suite
import unittest
import sqlalchemy
import models
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.models import Base, DeviceData

# Test for in memory SQLite
class TestSQLiteMemory(unittest.TestCase):
    # Database definition (in memory sqlite)
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()

    def setUp(self):
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        self.session.rollback()
        Base.metadata.drop_all(self.engine)

    def testCRUD(self):
        # Insert device type
        dd1 = DeviceData(value=10.0, datetimeRead=datetime.datetime.now())
        self.session.add(dd1)
        self.session.commit()

        # Check if inserted
        dd = self.session.query(DeviceData).filter_by(value=10.0).first()
        self.assertEquals(dd.value, dd1.value)

        # Check for non insertion
        dd = self.session.query(DeviceData).filter_by(value=99.0).first()
        self.assertTrue(dd is None)

        # Check Update
        dd = self.session.query(DeviceData).filter_by(value=10.0).first()
        dd.value = 20.0
        self.session.commit()
        ddTst = self.session.query(DeviceData).filter_by(value=20.0).first()
        self.assertEquals(ddTst.value, 20.0)

        # Check printout (to see this you have to run nosetest --nocapture
        dd = self.session.query(DeviceData).filter_by(value=20.0).first()
        print('DeviceData = %s' % dd)

        # Insert a second record and check insertion
        dd2 = DeviceData(value=100.0)
        self.session.add(dd2)
        self.session.commit()
        dd = self.session.query(DeviceData).filter_by(value=100.0).first()
        self.assertEquals(dd.value, dd2.value)

        # Rollback test
        dd3 = DeviceData(value=1000.0)
        self.session.add(dd3)
        self.session.rollback()
        dd = self.session.query(DeviceData).filter_by(value=1000.0).first()
        self.assertTrue(dd is None)

        # Delete record
        dd = self.session.query(DeviceData).filter_by(value=100.0).first()
        self.session.delete(dd)
        self.session.commit()
        self.assertTrue(self.session.query(DeviceData).filter_by(value=100.0).count()==0)

# Test for SQLite on local file
class TestSQLiteOnFile(unittest.TestCase):
    # Database definition
    engine = create_engine('sqlite:///test.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    

    def setUp(self):
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        self.session.rollback()
        Base.metadata.drop_all(self.engine)

    def testCRUD(self):
        # Insert device type
        dd1 = DeviceData(value=10.0, datetimeRead=datetime.datetime.now())
        self.session.add(dd1)
        self.session.commit()

        # Check if inserted
        dd = self.session.query(DeviceData).filter_by(value=10.0).first()
        self.assertEquals(dd.value, dd1.value)

        # Check for non insertion
        dd = self.session.query(DeviceData).filter_by(value=99.0).first()
        self.assertTrue(dd is None)

        # Check Update
        dd = self.session.query(DeviceData).filter_by(value=10.0).first()
        dd.value = 20.0
        self.session.commit()
        ddTst = self.session.query(DeviceData).filter_by(value=20.0).first()
        self.assertEquals(ddTst.value, 20.0)

        # Check printout (to see this you have to run nosetest --nocapture
        dd = self.session.query(DeviceData).filter_by(value=20.0).first()
        print('DeviceData = %s' % dd)

        # Insert a second record and check insertion
        dd2 = DeviceData(value=100.0)
        self.session.add(dd2)
        self.session.commit()
        dd = self.session.query(DeviceData).filter_by(value=100.0).first()
        self.assertEquals(dd.value, dd2.value)

        # Rollback test
        dd3 = DeviceData(value=1000.0)
        self.session.add(dd3)
        self.session.rollback()
        dd = self.session.query(DeviceData).filter_by(value=1000.0).first()
        self.assertTrue(dd is None)

        # Delete record
        dd = self.session.query(DeviceData).filter_by(value=100.0).first()
        self.session.delete(dd)
        self.session.commit()
        self.assertTrue(self.session.query(DeviceData).filter_by(value=100.0).count()==0)

# Test for mysql (tested on localhost with maria db)
class TestMySql(unittest.TestCase):
    # Database definition (be sure that the db name already exists in database)
    engine = create_engine('mysql://root:root@localhost/testsqlalchemy')
    Session = sessionmaker(bind=engine)
    session = Session()

    def setUp(self):
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        self.session.rollback()
        Base.metadata.drop_all(self.engine)

    def testCRUD(self):
        # Insert device type
        dd1 = DeviceData(value=10.0, datetimeRead=datetime.datetime.now())
        self.session.add(dd1)
        self.session.commit()

        # Check if inserted
        dd = self.session.query(DeviceData).filter_by(value=10.0).first()
        self.assertEquals(dd.value, dd1.value)

        # Check for non insertion
        dd = self.session.query(DeviceData).filter_by(value=99.0).first()
        self.assertTrue(dd is None)

        # Check Update
        dd = self.session.query(DeviceData).filter_by(value=10.0).first()
        dd.value = 20.0
        self.session.commit()
        ddTst = self.session.query(DeviceData).filter_by(value=20.0).first()
        self.assertEquals(ddTst.value, 20.0)

        # Check printout (to see this you have to run nosetest --nocapture
        dd = self.session.query(DeviceData).filter_by(value=20.0).first()
        print('DeviceData = %s' % dd)

        # Insert a second record and check insertion
        dd2 = DeviceData(value=100.0)
        self.session.add(dd2)
        self.session.commit()
        dd = self.session.query(DeviceData).filter_by(value=100.0).first()
        self.assertEquals(dd.value, dd2.value)

        # Rollback test
        dd3 = DeviceData(value=1000.0)
        self.session.add(dd3)
        self.session.rollback()
        dd = self.session.query(DeviceData).filter_by(value=1000.0).first()
        self.assertTrue(dd is None)

        # Delete record
        dd = self.session.query(DeviceData).filter_by(value=100.0).first()
        self.session.delete(dd)
        self.session.commit()
        self.assertTrue(self.session.query(DeviceData).filter_by(value=100.0).count()==0)
