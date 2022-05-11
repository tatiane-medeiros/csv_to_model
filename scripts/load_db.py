from tabela.models import Dataset
import pandas as pd

def run():
    Dataset.objects.all().delete()
    df = pd.read_csv('dataset.csv', sep=',')
    df = df.fillna('')

    for index, row in df.iterrows():
        it = Dataset(serie=row['serie'], nome=row['nome'], descricao=row['descrição'], fonte=row['fonte'])
        it.save()
