#!/usr/bin/env ruby

# Define a function to find and join occurrences of "School" in a string
def find_and_join_school_occurrences(input)
  input.scan(/School/).join
end

# Print the joined occurrences of "School" from the input argument
puts find_and_join_school_occurrences(ARGV[0])
