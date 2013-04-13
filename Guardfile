# Requirement
#  ruby
#  $ gem install guard
#  $ gem install guard-shell
#  $ guard

guard 'shell' do
  watch(%r{^.+\.py$}) do |m|
    puts "Files changed: #{m.inspect}"
    debug_prints = []
    m.map do |filename|
      if filename =~ %r{^tests/test_}
        debug_prints << `python #{filename}`
      else
        debug_prints << `python tests/all_test.py`
      end
    end
    debug_prints
  end
end

