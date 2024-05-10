#!/usr/bin/env ruby

# Define a function to scan for the pattern /hb?tn/ in the input string
def scan_pattern(input)
  input.scan(/hb?tn/)
end

# Print the result of scanning for the pattern in the input argument
puts scan_pattern(ARGV[0]).join(' ')
