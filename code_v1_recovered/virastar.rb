require 'rubygems'
require 'virastar'

my_file = ARGV[0].to_s

#open(my_file,"r:UTF-8") do |f|
open(my_file) do |f| 
  while line = f.gets
    newline = line.persian_cleanup
    puts newline
  end
end

