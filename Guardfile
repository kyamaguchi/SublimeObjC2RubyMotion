# Requirement
#  ruby
#  $ gem install guard
#  $ gem install guard-shell
#  $ guard

guard 'shell' do
  watch(%r{^.+\.py$}) do |m|
    puts "Files changed: #{m.inspect}"
    `python tests/all_test.py`
  end
end

