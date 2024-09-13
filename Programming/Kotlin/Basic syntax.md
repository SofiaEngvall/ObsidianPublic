
not changing var?
val age: Int = 25

normal var?
var name: String = "Unknown"

fun greet() {
  println("Hello!")
}

val name: String = "Sofia"
println("Hello, $name!")

if (age >= 18) {  
  println("You are an adult.")  
}

val day = "Monday"  
when (day) {  
  "Monday" -> println("Start of the week!")  
  "Friday" -> println("Almost weekend!")  
  else -> println("Just another day.")
}

for (i in 1..5) {  
  println(i)
}

var count = 5  
  while (count > 0) {  
  println(count)  
  count--  
}

var count = 5  
  do {  
  println(count)  
  count--  
} while (count > 0)

val numbers = arrayOf(1, 2, 3, 4, 5)  
for (number in numbers) {  
  println(number)  
}


