from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

# Calcula a média do filme
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1) 
        return None

# Validação do ano do filme
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value

# Validação de caracteres do resumo do filme
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não deve conter mais de 200 caracteres.')
        return value
