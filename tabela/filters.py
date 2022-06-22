from tabela.models import Dataset
import django_filters

class DataFilter(django_filters.FilterSet):
    #tipofonte = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Dataset
        fields = ['tipofonte']

    def __init__(self, *args, **kwargs):
        super(DataFilter, self).__init__(*args, **kwargs)
        self.filters['tipofonte'].label = 'Tipo de fonte'
