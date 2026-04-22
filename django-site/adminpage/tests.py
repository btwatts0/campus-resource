from django.test import TestCase
from .models import Resource


class ResourceModelTest(TestCase):
    def setUp(self):
        self.resource = Resource.objects.create(
            name="CSci Textbooks",
            category="Books",
            location="Meriam Library",
            desc="A collection of computer science textbooks available for short-term loan.",
            avail="Available",
        )

    def test_resource_creation(self):
        """A Resource object is saved with the correct field values."""
        resource = Resource.objects.get(id=self.resource.id)
        self.assertEqual(resource.name, "CSci Textbooks")
        self.assertEqual(resource.category, "Books")
        self.assertEqual(resource.location, "Meriam Library")
        self.assertEqual(resource.desc, "A collection of computer science textbooks available for short-term loan.")
        self.assertEqual(resource.avail, "Available")

    def test_category_choices(self):
        """Resource accepts each valid category choice."""
        valid_categories = ["Books", "Rooms", "Loanables", "Tutoring"]
        for category in valid_categories:
            resource = Resource.objects.create(
                name=f"Test {category}",
                category=category,
                location="Campus",
                desc="Test description.",
                avail="Available",
            )
            self.assertEqual(resource.category, category)

    def test_availability_choices(self):
        """Resource accepts each valid availability choice."""
        valid_avail = ["Available", "Limited", "Unavailable"]
        for avail in valid_avail:
            resource = Resource.objects.create(
                name=f"Resource {avail}",
                category="Rooms",
                location="Campus",
                desc="Test description.",
                avail=avail,
            )
            self.assertEqual(resource.avail, avail)

    def test_resource_count_after_creation(self):
        """Database contains the expected number of Resource records."""
        # setUp already created one resource
        self.assertEqual(Resource.objects.count(), 1)

    def test_resource_deletion(self):
        """Deleting a Resource removes it from the database."""
        resource_id = self.resource.id
        self.resource.delete()
        self.assertFalse(Resource.objects.filter(id=resource_id).exists())
