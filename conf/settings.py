# Bitmask for click
EVAL_CLICK = 1

# Bitmask for correct note
EVAL_NOTE  = 2

# Bitmask for correct scale
EVAL_SCALE = 4

# Bitmask for correct time
EVAL_TIME  = 8

# Where to read session files
SESSION_DIR = 'media/sessions'

# Where to write evaluation data
OUTPUT_DIR = 'media/data'

# Default file to take session
READ_FILE = 'test.csv'

# The default evaluation criteria, evaluate everything
EVALUATION_CRITERIA = EVAL_CLICK | EVAL_NOTE | EVAL_SCALE | EVAL_TIME

# Where to write output, one of ('file', 'console')
OUTPUT_ADAPTER = 'file'
