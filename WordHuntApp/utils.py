import datetime, pytz, exifread
from WordHuntApp.models import *
from django.contrib.auth.models import User
from registration.signals import user_registered
from django.core.signals import request_finished
from django.dispatch import receiver


def get_current_word():
    competition = Competition.objects.latest('start_date')
    word = competition.word

    return word


def is_competition_active():
    competition = Competition.objects.latest('start_date')
    now = datetime.datetime.now(pytz.utc)

    return competition.start_date < now < competition.end_date


# Convert the GPS coordinates from DMS (degrees, minutes, deconds) format
# to DD (degrees, degrees) format, which is more useful
def _convert_from_dms_to_dd(coords):
    # Convert one operand to float so we get float division
    degrees = float(coords.values[0].num) / coords.values[0].den
    minutes = float(coords.values[1].num) / coords.values[1].den
    seconds = float(coords.values[2].num) / coords.values[2].den

    return degrees + (minutes / 60.0) + (seconds / 3600.0)


def get_image_coordinates(path):
    image = open(path, 'rb')
    exif_tags = exifread.process_file(image, details=False)
    # Try to get GPS coordinates from EXIF data
    try:
        latitude_ref = exif_tags["GPS GPSLatitudeRef"]
        longitude_ref = exif_tags["GPS GPSLongitudeRef"]
        latitude = exif_tags["GPS GPSLatitude"]
        longitude = exif_tags["GPS GPSLongitude"]
    except KeyError:
        return False, False

    # If we don't have all the data, we cannot parse the coordinates
    if not (latitude and latitude_ref and longitude and longitude_ref):
        return False, False

    lat_dd = _convert_from_dms_to_dd(latitude)
    long_dd = _convert_from_dms_to_dd(longitude)
    if latitude_ref.values == 'S':
        lat_dd = -lat_dd
    if longitude_ref.values == 'W':
        long_dd = -long_dd

    return lat_dd, long_dd


def calculate_new_average_rating(image):
    image_ratings = Rating.objects.filter(image=image)
    image.avg_rating = sum(r.rating for r in image_ratings) / len(image_ratings)
    image.save()

    update_competition_ranks()


def update_competition_ranks():
    word = get_current_word()
    try:
        images = Image.objects.filter(related_word=word).order_by("-avg_rating")
        for comp_rank, image in enumerate(images, 1):
            user = UserProfile.objects.get(user=image.user)
            user.competition_rank = comp_rank
            user.save()

    except Image.DoesNotExist:
        print("No images yet for competition '%s'" % word.text)


def search_for_users(query):
    results = []
    for user in UserProfile.objects.all():
        if query in str(user).lower(): results.append(user)
    return results


def search_for_words(query):
    results = []
    for word in Word.objects.all():
        if query in str(word).lower(): results.append(word)
    return results


def get_number_of_user_images(user_profiles):
    numbers = []
    for user_profile in user_profiles:
        numbers.append(len(Image.objects.filter(user=user_profile.user)))
    return numbers

# Create a new UserProfile object for each newly registered user
@receiver(user_registered)
def create_new_user_profile(sender, **kwargs):
    user = kwargs["user"]
    user_profile = UserProfile.objects.create(user=user,
                                              rank=get_last_rank())
    print("New user successfully registered")


def get_last_rank():
    return len(UserProfile.objects.all()) + 1