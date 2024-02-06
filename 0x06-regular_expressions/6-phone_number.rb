#!/usr/bin/env ruby
# matches few etters in input
puts ARGV[0].scan(/\A\d{10}\z/).join
