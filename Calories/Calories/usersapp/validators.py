from django.core.exceptions import ValidationError


def image_max_size(value):
    filesize = value.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
