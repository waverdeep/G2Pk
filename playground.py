import fileIO
import useG2Pk


filepath = 'dataset/total_data.csv'
scripts = fileIO.read_csv_pandas(filepath=filepath)
g2pk_scripts = useG2Pk.convert_g2pk_scripts_pandas(scripts)
print(len(g2pk_scripts))
