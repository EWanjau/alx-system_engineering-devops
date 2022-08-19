#!/usr/bin/env ruby
# matches all hbt*tnwords in  the input 
puts ARGV[0].scan(/hbt{2,5}tn/).join
