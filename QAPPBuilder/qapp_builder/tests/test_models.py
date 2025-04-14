from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
from teams.models import Team
from qapp_builder.models import Qapp, QappSharingTeamMap, Revision, AcronymAbbreviation


class QappModelTest(TestCase):
    """Test cases for the Qapp model."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.team = Team.objects.create(
            name='Test Team',
            created_by=self.user,
            last_modified_by=self.user
        )
        self.qapp = Qapp.objects.create(
            title='Test QAPP',
            created_by=self.user
        )

    def test_qapp_creation(self):
        """Test QAPP creation with required fields."""
        self.assertEqual(self.qapp.title, 'Test QAPP')
        self.assertEqual(self.qapp.created_by, self.user)
        self.assertIsNotNone(self.qapp.created_on)
        self.assertIsNotNone(self.qapp.updated_on)

    def test_qapp_str_representation(self):
        """Test the string representation of QAPP."""
        self.assertEqual(str(self.qapp), 'Test QAPP')

    def test_qapp_progress_without_section(self):
        """Test getting QAPP progress without specifying a section."""
        progress = self.qapp.get_progress()
        self.assertIsInstance(progress, (int, float))

    def test_qapp_progress_with_section(self):
        """Test getting QAPP progress with a specific section."""
        progress = self.qapp.get_progress(section='section_a')
        self.assertEqual(progress, 0)  # Should return 0 for non-existent section


class QappSharingTeamMapTest(TestCase):
    """Test cases for the QappSharingTeamMap model."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.team = Team.objects.create(
            name='Test Team',
            created_by=self.user,
            last_modified_by=self.user
        )
        self.qapp = Qapp.objects.create(
            title='Test QAPP',
            created_by=self.user
        )
        self.sharing_map = QappSharingTeamMap.objects.create(
            qapp=self.qapp,
            team=self.team,
            can_edit=True
        )

    def test_sharing_map_creation(self):
        """Test QappSharingTeamMap creation with required fields."""
        self.assertEqual(self.sharing_map.qapp, self.qapp)
        self.assertEqual(self.sharing_map.team, self.team)
        self.assertTrue(self.sharing_map.can_edit)
        self.assertIsNotNone(self.sharing_map.added_date)

    def test_sharing_map_str_representation(self):
        """Test the string representation of QappSharingTeamMap."""
        expected_str = f'Team "{self.team}" - {self.qapp}'
        self.assertEqual(str(self.sharing_map), expected_str)


class RevisionTest(TestCase):
    """Test cases for the Revision model."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.team = Team.objects.create(
            name='Test Team',
            created_by=self.user,
            last_modified_by=self.user
        )
        self.qapp = Qapp.objects.create(
            title='Test QAPP',
            created_by=self.user
        )
        self.revision = Revision.objects.create(
            qapp=self.qapp,
            date=date.today(),
            author='Test Author',
            description='Test Revision Description'
        )

    def test_revision_creation(self):
        """Test Revision creation with required fields."""
        self.assertEqual(self.revision.qapp, self.qapp)
        self.assertEqual(self.revision.date, date.today())
        self.assertEqual(self.revision.author, 'Test Author')
        self.assertEqual(self.revision.description, 'Test Revision Description')


class AcronymAbbreviationTest(TestCase):
    """Test cases for the AcronymAbbreviation model."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.team = Team.objects.create(
            name='Test Team',
            created_by=self.user,
            last_modified_by=self.user
        )
        self.qapp = Qapp.objects.create(
            title='Test QAPP',
            created_by=self.user
        )
        self.acronym = AcronymAbbreviation.objects.create(
            qapp=self.qapp,
            acronym_abbreviation='EPA',
            definition='Environmental Protection Agency'
        )

    def test_acronym_creation(self):
        """Test AcronymAbbreviation creation with required fields."""
        self.assertEqual(self.acronym.qapp, self.qapp)
        self.assertEqual(self.acronym.acronym_abbreviation, 'EPA')
        self.assertEqual(self.acronym.definition, 'Environmental Protection Agency')

    def test_acronym_labels_property(self):
        """Test the labels property of AcronymAbbreviation."""
        expected_labels = {'acronym_abbreviation': 'Acronym/Abbreviation'}
        self.assertEqual(self.acronym.labels, expected_labels)