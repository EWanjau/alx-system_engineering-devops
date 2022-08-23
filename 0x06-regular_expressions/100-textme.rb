#!/usr/bin/env ruby
# matches few etters in input
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.?)\]\s\[flags:(.?)\]/).join(',')
