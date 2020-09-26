
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class User(AbstractUser):

    username = models.CharField(
        _('username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("Username already taken."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True,
                              error_messages={
                                  'unique': _("A user with that email already exists.")
                              })
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    login_count = models.IntegerField(editable=False, default=0)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class UserProfile(models.Model):
    """
    This will serve as link to our user class.
    This will also have common attributes across user types.
    """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="%(class)s", primary_key=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    zip = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=30, null=True, blank=True)
    dob = models.DateField(_('Date of Birth'), null=True, blank=True)
    aadhar = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract = True

    def get_address(self):
        address = "%s, %s, %s %s" % (self.city, self.state, self.country, self.zip)
        return address

class Student(UserProfile):
    registration_numner = models.CharField(_('Registration Number'), max_length=250, null=True, blank=True)
    is_passed = models.BooleanField(null=True, default=False)
    total_marks = models.IntegerField(_('Total Marks'), null=True, blank=True, default=1000)
    marks_obtained = models.IntegerField(_('Marks Obtained'), null=True, blank=True, default=0)




    def __str__(self):
        return "%s" % self.user.email

    def get_pass_status(self):
        if self.is_passed:
            return "Passed"
        else:
            return "Failed"

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")
