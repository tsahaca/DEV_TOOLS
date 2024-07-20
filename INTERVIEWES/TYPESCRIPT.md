# TypeScript Interview Questions and Answers

## Basic Questions

### What is TypeScript and how does it differ from JavaScript?
**Answer**: TypeScript is a superset of JavaScript that adds static typing to the language. It compiles to plain JavaScript. TypeScript provides features like type annotations, interfaces, and type inference which are not available in JavaScript, making it easier to catch errors at compile time and write more robust code.

### What are the benefits of using TypeScript?
**Answer**: The benefits include static typing, enhanced IDE support, improved code quality and maintainability, better tooling, scalability for large projects, incremental adoption, robust ecosystem, better debugging, consistent code style, future-proofing, and wide industry adoption.

### How do you install TypeScript?
**Answer**: TypeScript can be installed globally using npm (Node Package Manager) with the command `npm install -g typescript`. You can then use the `tsc` command to compile TypeScript files.

### What is a `.d.ts` file in TypeScript?
**Answer**: A `.d.ts` file is a TypeScript declaration file. It is used to describe the shape of JavaScript libraries, providing TypeScript with information about the types in a JavaScript codebase. These files help TypeScript understand the types used in external libraries without actually providing the implementation.

## Intermediate Questions

### What is the purpose of `tsconfig.json`?
**Answer**: `tsconfig.json` is a configuration file for TypeScript. It specifies the root files and the compiler options required to compile the project. The file helps in setting up the TypeScript project with options like target ECMAScript version, module system, and more.

### Explain the difference between `interface` and `type` in TypeScript.
**Answer**: Both `interface` and `type` can be used to define the shape of an object. Interfaces can be extended or implemented by classes, and they support declaration merging. Types are more flexible and can represent other constructs like unions, intersections, and primitives, but they cannot be re-opened for adding properties.

### What are generics in TypeScript and how do you use them?
**Answer**: Generics provide a way to create reusable components that work with a variety of types instead of a single one. You define a generic by using angle brackets (`<>`) and a type variable, which can then be used throughout the component. Example:
```typescript
function identity<T>(arg: T): T {
  return arg;
}
let output = identity<string>("Hello");
