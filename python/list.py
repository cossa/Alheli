#Homogeneus list

integers = [1, 2 ,3 , 8, 33]

animals = ["dog", "cat", "goat"]

names = ["Roger", "Pame", "Manfred"]

floats = [2.2, 4.5, 9.8, 10.8]

#Heterogeneus List

numbers_animals_names = [2, "cat", 34.33, "Poller"]


list_lists =[[1, 2, 3],["cat", "dog", "chicken"]]

#How to access an element in a list
 
list = [3, 22, 30, 5.3,20]
 
print(list[2])
print(list[0])
print(list[1])
print(list[4])
 
 #200 words
 
words =  [
    "Function", "Variable", "Loop", "Condition", "Module", "Class", "Object", 
    "Method", "List", "Dictionary", "Tuple", "Set", "String", "Integer", 
    "Float", "Boolean", "Exception", "Import", "Package", "Library", "Syntax", 
    "Indentation", "Comment", "Argument", "Parameter", "Return", "Iterate", 
    "Range", "Comprehension", "Decorator", "Generator", "Lambda", "Closure", 
    "Scope", "Namespace", "Keyword", "Statement", "Expression", "Tuple", "Slice", 
    "Map", "Filter", "Reduce", "Import", "Virtual", "Environment", "Debug", 
    "Compile", "Interpreter", "REPL", "JSON", "CSV", "API", "Framework", 
    "Django", "Flask", "NumPy", "Pandas", "Matplotlib", "TensorFlow", "Keras", 
    "SciPy", "PyTorch", "Web", "Socket", "Thread", "Asynchronous", "Promise", 
    "Callback", "Queue", "Semaphore", "Lock", "Fork", "Process", "Memory", 
    "Garbage", "Collection", "Reference", "Pointer", "Attribute", "Instance", 
    "Inheritance", "Polymorphism", "Encapsulation", "Abstraction", "Design", 
    "Pattern", "Prototype", "Interface", "API", "Endpoint", "Request", 
    "Response", "Server", "Client", "URL", "Path", "Route", "Middleware", 
    "Session", "Cookie", "Token", "Authentication", "Authorization", 
    "Encryption", "Hashing", "SSL", "TLS", "Deployment", "Hosting", 
    "Continuous", "Integration", "Delivery", "Version", "Control", "Git", 
    "Repository", "Branch", "Commit", "Merge", "Conflict", "Pull", "Push", 
    "Clone", "Fork", "Fetch", "Stash", "Log", "Diff", "Remote", "Local", 
    "History", "Bug", "Feature", "Task", "Sprint", "Agile", "Kanban", 
    "Scrum", "Review", "Refactor", "Test", "Unit", "Integration", "System", 
    "Coverage", "Framework", "Assertion", "Mock", "Patch", "Setup", "TearDown", 
    "Fixture", "Run", "CLI", "ArgumentParser", "Docstring", "Type", 
    "Hint", "Annotations", "Context", "Manager", "File", "Input", "Output", 
    "Read", "Write", "Open", "Close", "Stream", "Buffer", "Exception", 
    "Traceback", "Raise", "Try", "Except", "Finally", "With", "Context", 
    "Manager", "JSON", "YAML", "XML", "SQL", "ORM", "Query", "Database", 
    "Transaction", "Migration", "Schema", "Field", "Record", "Join", "Index", 
    "View", "Controller", "Model", "REST", "GraphQL", "CRUD"
]

print(words[-1])

#list slicing

list = [3, 22, 30, 5.3, 20]

print(list[:])

print(list[1:3])

print(list[2:-1])

#update a list

science = ["art", "chemistry", "math"]
science [0] = "biology"
science [2] = "geology"

print(science)

integers = [2, 5, 9, 20, 27]
integers.remove(5)

print(integers)

integers.remove (27)
print (integers)

integers.pop()
print(integers)

list_fruits = ["avocado", "watermelon", "melon"]
#pop, remove, del

del list_fruits[0]
print(list_fruits)

list_names = ["Jhon", "Paul", "Pame"]

list_names.append("Roger")
print(list_names)

my_list = ["a", "b", "c", "d"]

print(my_list.index("c"))

my_list = ["a", "v", ""]
