from .models import Hotel
from modeltranslation.translator import TranslationOptions, register


@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'hotel_description', 'country', 'city', 'address')
