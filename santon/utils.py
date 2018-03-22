from cStringIO import StringIO
import csv
import os

from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.template.loader import get_template
from django.utils.text import slugify

from PIL import Image as pil


def construct_choices(items, sort=True, label=None, slug=False):
    """Constructs a tuple from a list and optionally sorts it, appends a label
    or slugifies the value.
    """
    if sort:
        items.sort()
    if label is not None:
        items.insert(0, label)
    if slug:
        return [[slugify(item), item] for item in items]
    return [[item, item] for item in items]


def generate_csv(data_list, file_name):
    """Generates a csv given a list of lists and a file name.
    """
    csv_file = StringIO()
    csv_writer = csv.writer(
        csv_file, dialect="excel", quotechar="\"", quoting=csv.QUOTE_ALL
    )
    for data in data_list:
        csv_writer.writerow(data)
    return file_name, csv_file.getvalue(), "text/csv"


def render_email_template(template_name, context_data=None):
    """Renders an email message from a template with optional context data.
    """
    context_data = context_data or {}
    template = get_template(template_name)
    return template.render(context_data)


def send_email(subject, body, to, **kwargs):
    """Generic email function which uses sane defaults in settings to populate
    certain params of the django email class.
    """
    email_message = EmailMessage(
        subject=subject, body=body, to=to, **kwargs
    )
    return email_message.send(fail_silently=False)


def image_resize(image, width=None, height=None):
    """Resizes images on the fly -cropping from the centre. If width and height
    args are 0 (zero) or None they will be ignored. Images that are smaller
    than the required dimensions are returned as is and if the image file
    doesn't exist no-iamge.png is returned instead.
    """
    if not image:
        return static("img/no-image.jpg")

    image_base, image_ext = os.path.splitext(image.path)

    # Use the dimensions to construct the resized images path
    path_extra = "_%s%s%s" % (
        width or "", "_" if width and height else "", height or ""
    )
    resized_image_path = "".join([image_base, path_extra, image_ext])

    # Get the image url
    resized_image_url = "".join(
        [os.path.splitext(image.url)[0], path_extra, image_ext]
    )

    # Check if resized image and stored image exists for use - double check
    # permissions are correct
    if os.path.exists(resized_image_path):
        return resized_image_url

    if not os.path.exists(image.path):
        return static("img/no-image.jpg")

    # Open the file and store the format
    image_file = pil.open(image.path)
    image_format = image_file.format

    # Store the original image width and height
    image_width, image_height = image_file.size

    # Use the original size if no size given
    resized_image_width = float(width or image_width)
    resized_image_height = float(height or image_height)

    # Find the closest bigger proportion to the maximum size
    image_scale = max(
        resized_image_width / float(image_width),
        resized_image_height / float(image_height)
    )

    # Return the original image if it is smaller than the required dimensions
    if image_scale > 1:
        return image.url

    # If the image is not bigger than the original size, calculate proportions
    # and resize
    resized_width = int(image_width * image_scale)
    resized_height = int(image_height * image_scale)
    resized_image = image_file.resize(
        (resized_width, resized_height), pil.ANTIALIAS
    )

    # Crop the image as required
    crop_left = int((resized_width - resized_image_width) / 2)
    crop_top = int((resized_height - resized_image_height) / 2)
    crop_right = int(crop_left + resized_image_width)
    crop_bottom = int(crop_top + resized_image_height)
    resized_image = resized_image.crop(
        (crop_left, crop_top, crop_right, crop_bottom)
    )

    # Save the image object
    resized_image.save(resized_image_path, image_format, quality=95)

    # Change the image file permissions
    os.chmod(resized_image_path, 0755)

    return resized_image_url
