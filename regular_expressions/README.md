This repository, named alu-scripting, is a collection of Ruby scripts utilizing regular expressions. Each script focuses on different patterns using the scan method to extract specific text from the provided input.

Regular Exp
The scripts are designed to showcase regular expressions in the context of pattern matching within text data.

Usage
To run these scripts, ensure you have Ruby installed on your system. Execute each script by passing the desired text as a command-line argument.

Examples:
First Script:

#!/usr/bin/env ruby
puts ARGV[0].scan(/School/).join
This script scans the input for the word "School" and prints the result.

Second Script:

#!/usr/bin/env ruby
puts ARGV[0].scan(/hbt{2,5}n/).join
It searches for patterns with 'hbt' followed by 2 to 5 't' and ending with 'n'.

Third Script:

#!/usr/bin/env ruby
puts ARGV[0].scan(/hb?tn/).join
This script looks for patterns with 'hbt', an optional 'b', and 'tn'.

Fourth Script:

#!/usr/bin/env ruby
puts ARGV[0].scan(/hbt{1,5}n/).join
Searches for patterns with 'hbt' followed by 1 to 5 't' and ending with 'n'.

Fifth Script:

#!/usr/bin/env ruby
puts ARGV[0].scan(/hbt*n/).join
This script matches patterns with 'hbt' followed by zero or more 't' and ending with 'n'.


