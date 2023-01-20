import datetime as dt
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from reviews.models import Category, Genre, Title, User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=254)
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    role = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
        extra_kwargs = {
            'username': {
                'validators': [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message='Такой пользователь уже существует'
                    )
                ]
            }
        }
        
    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" не разрешено.'
            )
        return value

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'slug': {
                'validators': [
                    UniqueValidator(
                        queryset=Category.objects.all(),
                        message='Такой слаг уже существует'
                    )
                ]
            }
        }


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
        extra_kwargs = {
            'slug': {
                'validators': [
                    UniqueValidator(
                        queryset=Genre.objects.all(),
                        message='Такой слаг уже существует'
                    )
                ]
            }
        }


class TitleSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    genre = serializers.SlugField(many=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')

    def validate_year(self, value):
        year_now = dt.date.today().year
        if not (value <= year_now):
            raise serializers.ValidationError('Проверьте год выпуска!')
        return value

    def validate_genre(self, value):
        if not Genre.objects.filter(name=f'{value}').exists():
            raise serializers.ValidationError(
                'Выберите жанр из ранее созданных!')
        return value

    def validate_category(self, value):
        if not Category.objects.filter(name=f'{value}').exists():
            raise serializers.ValidationError(
                'Выберите категорию из ранее созданных!')
        return value
