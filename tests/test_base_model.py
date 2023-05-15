import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        # Test the initialization of BaseModel
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsInstance(base_model.created_at, datetime.datetime)
        self.assertIsInstance(base_model.updated_at, datetime.datetime)

    def test_to_dict(self):
        # Test the to_dict method of BaseModel
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)

    # Add more test methods for other functionalities in BaseModel

if __name__ == '__main__':
    unittest.main()
