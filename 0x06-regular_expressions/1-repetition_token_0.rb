#!/usr/bin/env ruby

# Define a function to match the pattern /hbt{2,5}n/ in the input string
def match_pattern(input)
  input.match(/hbt{2,5}n/)
end

# Print the result of matching the pattern in the input argument
puts match_pattern(ARGV[0])
