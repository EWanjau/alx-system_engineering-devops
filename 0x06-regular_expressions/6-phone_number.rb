#!/usr/bin/env ruby
# matches few etters in input
puts ARGV[0].scan(/^\d{10}/).join
