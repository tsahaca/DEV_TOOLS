### TypeScript Interview Questions and Answers

#### Basic Questions

**Q1: What is TypeScript?**

**A:** TypeScript is an open-source programming language developed and maintained by Microsoft. It is a superset of JavaScript that adds static typing, classes, and interfaces. TypeScript compiles to plain JavaScript, ensuring compatibility with existing JavaScript code and libraries.

**Q2: What are the advantages of using TypeScript over JavaScript?**

**A:**
- **Static Typing:** TypeScript's static typing helps catch errors at compile-time rather than runtime.
- **Improved IDE Support:** TypeScript provides better code completion, refactoring, and navigation.
- **Readability and Maintainability:** Type annotations improve the readability and maintainability of the code.
- **Advanced Features:** TypeScript includes advanced features like interfaces, generics, and decorators.
- **Compatibility:** TypeScript is backward compatible with JavaScript.

**Q3: How do you install TypeScript?**

**A:** You can install TypeScript globally using npm (Node Package Manager) with the following command:
```bash
npm install -g typescript
```

#### Advanced Questions

**Q4: Explain the TypeScript type system.**

**A:** TypeScript's type system is structural, meaning it relies on the shape that values have. Types can be:
- **Primitive Types:** `string`, `number`, `boolean`, `null`, `undefined`, `symbol`, `bigint`.
- **Object Types:** Complex types like objects, arrays, functions, etc.
- **Union Types:** A value that can be one of several types (e.g., `string | number`).
- **Intersection Types:** Combines multiple types into one (e.g., `TypeA & TypeB`).
- **Generics:** Allow creating reusable components that work with any type.
- **Type Aliases:** Custom names for types (e.g., `type MyType = string | number`).
- **Interfaces:** Define the shape of an object (e.g., `interface Person { name: string; age: number; }`).

**Q5: What are decorators in TypeScript?**

**A:** Decorators are a special kind of declaration that can be attached to a class, method, accessor, property, or parameter. Decorators are used to modify or augment the behavior of the target they are attached to. They are currently an experimental feature in TypeScript and are used extensively in frameworks like Angular.

Example of a class decorator:
```typescript
function logClass(target: Function) {
  console.log(`Class ${target.name} was created.`);
}

@logClass
class MyClass {
  constructor() {
    console.log('MyClass instance created.');
  }
}
```

**Q6: Explain the concept of "interfaces" in TypeScript.**

**A:** Interfaces in TypeScript define the structure that an object should conform to. They are used to define the types of properties, methods, and events in an object.

Example:
```typescript
interface Person {
  name: string;
  age: number;
  greet(): void;
}

const person: Person = {
  name: 'John',
  age: 30,
  greet() {
    console.log(`Hello, my name is ${this.name}`);
  }
};

person.greet(); // Output: Hello, my name is John
```

**Q7: What are generics in TypeScript and why are they used?**

**A:** Generics provide a way to create reusable components that can work with a variety of data types while maintaining type safety. They allow you to write a function, class, or interface that can work with different data types without sacrificing the type safety.

Example:
```typescript
function identity<T>(arg: T): T {
  return arg;
}

const output1 = identity<string>('Hello');
const output2 = identity<number>(42);
```

#### Practical Questions

**Q8: How do you configure TypeScript projects using `tsconfig.json`?**

**A:** The `tsconfig.json` file is used to configure TypeScript compiler options. Here’s an example:
```json
{
  "compilerOptions": {
    "target": "ES6",
    "module": "commonjs",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true
  },
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules"]
}
```
- **target:** Specifies the ECMAScript target version.
- **module:** Specifies the module system.
- **outDir:** Output directory for compiled files.
- **rootDir:** Root directory of source files.
- **strict:** Enable all strict type-checking options.
- **esModuleInterop:** Enable interoperability between CommonJS and ES Modules.

**Q9: How can you extend an interface in TypeScript?**

**A:** You can extend an interface using the `extends` keyword.

Example:
```typescript
interface Animal {
  name: string;
  age: number;
}

interface Dog extends Animal {
  breed: string;
}

const myDog: Dog = {
  name: 'Buddy',
  age: 5,
  breed: 'Golden Retriever'
};
```

**Q10: How do you handle modules in TypeScript?**

**A:** TypeScript uses ES6 module syntax for import and export. You can export any variable, function, class, or interface from a module and import them into another module.

Example:
- **Module file (module.ts):**
  ```typescript
  export const PI = 3.14;

  export function calculateCircumference(diameter: number): number {
    return diameter * PI;
  }
  ```

- **Importing module (main.ts):**
  ```typescript
  import { PI, calculateCircumference } from './module';

  console.log(`Circumference: ${calculateCircumference(10)}`); // Output: Circumference: 31.4
  ```

These questions and answers cover a broad range of topics, from basic concepts to more advanced and practical scenarios, providing a comprehensive understanding of TypeScript for interview preparation.

In TypeScript, `any` and `undefined` are two distinct types that serve different purposes. Understanding their differences and appropriate usage is essential for writing robust TypeScript code.

### `any` Type

- **Description:** The `any` type is a type that disables TypeScript's type checking. When a variable is declared with the `any` type, it can hold any value, and TypeScript will not enforce any type checks on it.
- **Use Cases:** It is typically used when you need to work with dynamic content, such as data from external sources (like JSON responses) where the exact type is unknown or when migrating JavaScript code to TypeScript.
- **Example:**

  ```typescript
  let value: any;
  value = 42;         // OK
  value = "hello";    // OK
  value = true;       // OK
  value.someMethod(); // OK (no type checking)
  ```

- **Pros:**
  - Flexibility in handling dynamic data.
  - Useful for quick prototyping or when migrating from JavaScript.

- **Cons:**
  - Disables type safety, potentially leading to runtime errors.
  - Makes code harder to maintain and understand.

### `undefined` Type

- **Description:** The `undefined` type represents a value that has not been assigned. In JavaScript and TypeScript, `undefined` is a primitive value that signifies the absence of a value.
- **Use Cases:** Typically used to denote uninitialized variables or optional properties that have not been provided.
- **Example:**

  ```typescript
  let value: undefined;
  value = undefined;  // OK
  value = 42;         // Error: Type '42' is not assignable to type 'undefined'

  let maybeValue: number | undefined;
  maybeValue = 42;         // OK
  maybeValue = undefined;  // OK
  ```

- **Pros:**
  - Explicitly represents uninitialized or absent values.
  - Useful in conjunction with strict null checks (`strictNullChecks` option in TypeScript).

- **Cons:**
  - Can be confusing when mixed with `null`, which also represents an absence of value but is a distinct type.
  - Overuse can lead to unclear code, especially if not handled properly.

### Comparison

- **Type Safety:**
  - `any`: Disables type checking, offering no type safety.
  - `undefined`: Part of the strict type system, providing better type safety when used correctly.

- **Use Case Specificity:**
  - `any`: Best used for dynamic or loosely typed scenarios.
  - `undefined`: Best used for explicitly uninitialized values or optional properties.

- **Code Maintenance:**
  - `any`: Can lead to maintenance challenges due to lack of type information.
  - `undefined`: Easier to maintain as part of a strictly typed system.

### Practical Example

Consider a function that processes user input, which can be of any type, versus handling a function parameter that might be missing:

```typescript
function processInput(input: any) {
  // No type checking on input
  console.log(input.toUpperCase()); // Potential runtime error if input is not a string
}

function greet(name: string | undefined) {
  if (name === undefined) {
    console.log("Hello, Guest!");
  } else {
    console.log(`Hello, ${name}!`);
  }
}

processInput(42); // No compile-time error, but runtime error
greet(undefined); // Safe handling of undefined value
```

In summary, `any` is a flexible but type-unsafe way to handle values of any type, while `undefined` is a type-safe way to represent uninitialized or absent values in TypeScript. Using `any` should be minimized to maintain type safety and code quality.
