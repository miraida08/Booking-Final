from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'


class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user_name', 'text', 'hotel_stars']


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class HotelListSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'city', 'hotel_image', 'stars', 'average_rating']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class RoomListSerializer(serializers.ModelSerializer):
    room_image = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'room_status', 'room_price', 'room_image', 'all_inclusive']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializer(many=True, read_only=True)
    reviews = ReviewListSerializer(many=True, read_only=True)
    rooms = RoomListSerializer(many=True, read_only=True)
    owner = UserProfileSerializer(read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'hotel_description', 'country', 'city', 'address', 'stars',
                 'hotel_image', 'hotel_video', 'reviews', 'created_date', 'owner', 'rooms', 'average_rating']

    def get_average_rating(self, obj):
        return obj.get_average_rating()






