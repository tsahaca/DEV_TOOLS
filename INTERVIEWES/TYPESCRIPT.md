# Typescript Interview Questions

Basic Questions
What is TypeScript and how does it differ from JavaScript?

Answer: TypeScript is a superset of JavaScript that adds static typing to the language. It compiles to plain JavaScript. TypeScript provides features like type annotations, interfaces, and type inference which are not available in JavaScript, making it easier to catch errors at compile time and write more robust code.
What are the benefits of using TypeScript?

Answer: The benefits include static typing, enhanced IDE support, improved code quality and maintainability, better tooling, scalability for large projects, incremental adoption, robust ecosystem, better debugging, consistent code style, future-proofing, and wide industry adoption.
How do you install TypeScript?

Answer: TypeScript can be installed globally using npm (Node Package Manager) with the command npm install -g typescript. You can then use the tsc command to compile TypeScript files.
What is a .d.ts file in TypeScript?

Answer: A .d.ts file is a TypeScript declaration file. It is used to describe the shape of JavaScript libraries, providing TypeScript with information about the types in a JavaScript codebase. These files help TypeScript understand the types used in external libraries without actually providing the implementation.
Intermediate Questions
What is the purpose of tsconfig.json?

Answer: tsconfig.json is a configuration file for TypeScript. It specifies the root files and the compiler options required to compile the project. The file helps in setting up the TypeScript project with options like target ECMAScript version, module system, and more.
Explain the difference between interface and type in TypeScript.

Answer: Both interface and type can be used to define the shape of an object. Interfaces can be extended or implemented by classes, and they support declaration merging. Types are more flexible and can represent other constructs like unions, intersections, and primitives, but they cannot be re-opened for adding properties.
What are generics in TypeScript and how do you use them?

Answer: Generics provide a way to create reusable components that work with a variety of types instead of a single one. You define a generic by using angle brackets (<>) and a type variable, which can then be used throughout the component. Example:
typescript
Copy code
function identity<T>(arg: T): T {
  return arg;
}
let output = identity<string>("Hello");
What is the any type and when should it be used?

Answer: The any type in TypeScript is a type that can hold any value, effectively opting out of type checking. It should be used sparingly, typically when interacting with dynamic content or third-party libraries where the types are not known or not declared.
Advanced Questions
What is type inference in TypeScript?

Answer: Type inference is the ability of TypeScript to automatically deduce the types of variables and function return values based on the assigned values. This helps reduce the need for explicit type annotations, making the code cleaner and easier to read.
Explain the difference between unknown and any in TypeScript.

Answer: The unknown type is similar to any in that it can hold any value, but it is safer because it forces the developer to perform type checks before performing operations on the value. This ensures better type safety compared to any.
What are decorators in TypeScript and how are they used?

Answer: Decorators are a special kind of declaration that can be attached to classes, methods, accessors, properties, or parameters. They are used to modify the behavior of these elements. Decorators are a feature of TypeScript used extensively in frameworks like Angular. Example of a class decorator:
typescript
Copy code
function sealed(constructor: Function) {
  Object.seal(constructor);
  Object.seal(constructor.prototype);
}
@sealed
class MyClass {}
How does TypeScript support module resolution?

Answer: TypeScript supports module resolution strategies that determine how the compiler finds the referenced modules. The two strategies are Classic and Node. The Classic strategy is similar to the resolution used in ECMAScript modules, while the Node strategy follows the module resolution used by Node.js.
What are union and intersection types in TypeScript?

Answer: Union types allow a variable to be one of several types, specified using the | symbol. Intersection types combine multiple types into one, specified using the & symbol. Example:
typescript
Copy code
type UnionType = string | number;
type IntersectionType = { name: string } & { age: number };
What are mapped types in TypeScript?

Answer: Mapped types allow you to create new types by transforming properties of an existing type. They use a syntax that resembles array or object literals but with type variables. Example:
typescript
Copy code
type Readonly<T> = { readonly [P in keyof T]: T[P] };
These questions cover a range of topics from basic to advanced, helping to assess a candidate's understanding and proficiency in TypeScript.
