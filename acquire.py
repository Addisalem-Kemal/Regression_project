import env
import pandas as pd


def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


query = '''select
	        * from properties_2017
            join predictions_2017
            using (parcelid)
            left join propertylandusetype
            using (propertylandusetypeid)
            where propertylandusedesc IN ("Single Family Residential",
                              "Inferred Single Family Residential") and transactiondate like "2017%"
'''

df = pd.read_sql(query, get_connection('zillow'))
