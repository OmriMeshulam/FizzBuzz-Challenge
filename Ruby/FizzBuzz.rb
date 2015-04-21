class FizzBuzz
  attr_reader :num1, :num2

  def initialize(num1, num2)
    @num1, @num2 = num1, num2
  end

  def run
    1.upto(100).each do |i|
      if i % num1 == 0 && i % num2 == 0
        puts "fizbuzz"
      elsif i % num1 == 0
        puts "fizz"
      elsif i % num2 == 0
        puts "buzz"
      else puts i
      end
    end
  end
end

fb = FizzBuzz.new(3, 5)
fb.run