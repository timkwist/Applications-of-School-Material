def total_probability_formula(b_given_a, a)
	if b_given_a.length == a.length
		sum = a.inject(:+)
		if sum != 1
			for i in 0...a.length
				puts "Old value of a#{i}: #{a[i]}"
				a[i] = a[i] / sum
				puts "New value of a#{i}: #{a[i]}"
			end
			puts "Total value: #{a.inject(:+)}"
		end
		probability_of_b = 0
		for i in 0...b_given_a.length
			probability_of_b += (b_given_a[i]) * (a[i])
		end
		return probability_of_b
	else
		print "Number of B given A variables was not equal to the number of A variables"
		return ""
	end
end
# Order: C vs Christie, C vs Paul, C vs Bush, C vs Huckabee, C vs Cruz, C vs Rubio, C vs Carson, C vs Trump
b_given_a = [0.503, 0.468, 0.462, 0.483, 0.480, 0.455, 0.473, 0.486]
a = [0.028, 0.028, 0.092, 0.044,0.072, 0.062, 0.132, 0.272]
print "Hilary Clinton's estimated probability of winning the general election, considered against 8 of the current GOP candidates: #{total_probability_formula(b_given_a, a) * 100}"