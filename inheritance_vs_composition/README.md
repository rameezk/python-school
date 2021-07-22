# Inheritance VS Composition

## Inheritance
- We still have some code duplication (all commission subclasses do the same thing)
- We have tight coupling (`HourlyEmployeeWithCommission` relies strictly on `HourlyEmployee`)
- If we need to extend the functionality but adding a new type of Employee, we will need to add multiple subclasses (e.g. if the new employee type can also be paid a commission)

## Composition
- An `Employee` can have a commission associated to it (it is composed rather than a direct descendant in a hierarchy)
- At most, we have one level of inheritance
- Adding a new `Contract` is easy and no modifications are needed to the `Employee` class