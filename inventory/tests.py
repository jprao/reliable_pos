from django.test import TestCase

from inventory.models import Category


class CategoryTestCase(TestCase):
    """
    Testcase for Category model
    """

    # def setUp(self)
    #     # Category.objects.create(name="Applications", active=True)
    #     # Category.objects.create(name="Hardware", active=True)

    def test_category_saved_sucessfully(self):
        cat = Category.objects.create(name="Applications", active=True)
        retrieved_cat = Category.objects.get(pk=cat.id)
        self.assertEqual(cat.name, retrieved_cat.name)

    def test_category_empty_active_should_be_set_to_true(self):
        cat = Category.objects.create(name="Not Setting active")
        retrieved_cat = Category.objects.get(pk=cat.id)
        self.assertEqual(retrieved_cat.active, True)

    def test_category_active_set_to_false_should_be_false(self):
        cat = Category.objects.create(name="Not Setting active", active=False)
        retrieved_cat = Category.objects.get(pk=cat.id)
        self.assertEqual(retrieved_cat.active, False)
