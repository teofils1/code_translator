from translator import Translator

translator = Translator()

ruby_code = """
class HelloWorld
  attr_accessor :name
  
  def initialize(name)
    @name = name
  end
  
  def greet
    if @name
      puts "Hello, #{@name}"
    else
      puts "Hello, World"
    end
  end
end

hello = HelloWorld.new("Alice")
hello.greet

# A loop example with range
for i in 1..5
  puts i
end
"""

python_code = translator.translate(ruby_code)
print(python_code)