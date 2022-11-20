def label_formatter(filename):
    '''
    Format the label as the follow:
        -lower case
        -starting and ending whitespace removed
        -replace the _ with a single whitespace between words
    '''
    return filename.split('0')[0].replace('_',' ').strip().lower()