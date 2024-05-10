#!/usr/bin/env ruby

# Define a method to extract information based on specific patterns from the input string
def extract_information(input)
  input.scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(',')
end

# Print the extracted information from the input argument
puts extract_information(ARGV[0])
