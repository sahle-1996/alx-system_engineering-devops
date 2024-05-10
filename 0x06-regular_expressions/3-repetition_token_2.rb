#!/usr/bin/env ruby

# Define a method to scan for the pattern /hbt+n/ in the input string
def scan_pattern(input)
  input.scan(/hbt+n/)
end

# Print the result of scanning for the pattern in the input argument
puts scan_pattern(ARGV[0]).join(' ')
