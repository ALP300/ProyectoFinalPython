"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
datos= pd.read_csv('ATP.csv')
df= pd.DataFrame(datos)
df.reset_index().to_csv('DatosExportadosATP.csv', header=True,
                        index=False)
df= datos.loc['Melbourne']
df.reset_index().to_csv('MelbourneSeleccATP.csv', header=True,
                        index=False)