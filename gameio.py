from datetime import datetime

def csv_result(essay):
    """Given the essay evaluation matrix return the string to be written to
    output file"""
    def to_line(val):
        return ','.join(map(str, val))+'\n'
    return map(to_line, essay)

def get_out_name(sess_name):
    """Compute the name for the output file given the input file name"""
    base = '.'.join(sess_name.split('.')[:-1])
    return '%s_output_%s.csv'%(base, datetime.now().strftime('%Y-%m-%dT%H-%M-%S'))
