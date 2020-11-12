import fileIO
import useG2Pk


filepath = 'dataset/total_data.csv'
output_filepath = 'dataset/g2pk_script.csv'
output_filepath = 'dataset/g2pk_script_with_label.csv'
scripts = fileIO.read_csv_pandas(filepath=filepath)
g2pk_scripts = useG2Pk.convert_g2pk_scripts_pandas(scripts)
print(len(g2pk_scripts))

fileIO.write_csv_file_with_type(output_filepath, g2pk_scripts)
fileIO.write_csv_file_with_type(output_filepath, g2pk_scripts, header=['x', 'y'])
