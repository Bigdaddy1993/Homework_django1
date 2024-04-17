from django.conf import settings
from django.core.cache import cache

from catalog.models import Version


def get_cached_subjects_for_products(product_pk):
    if settings.CACHE_ENABLED:
        key = f'subject_list_{product_pk}'
        subject_list = cache.get(key)
        if subject_list is None:
            subject_list = Version.objects.filter(product__pk=product_pk)
            cache.set(key, subject_list)
    else:
        subject_list = Version.objects.filter(product__pk=product_pk)

    return subject_list
