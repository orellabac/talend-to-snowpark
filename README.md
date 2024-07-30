# talend-to-snowpark

This is small set of scripts to aid in the accelaration of converting Scripts from Talend to Snowpark

The general approach is that you can take your talend xml export scripts and put them on an input folder.

Then you can call the tool like:

`python main.py --input file/or_folder --output file_or_folder`

The tool will assume that for each component there is a corresponding python file that implements the conversion logic.

This is a work in progress so right now conversion capabilities are very basicz`
